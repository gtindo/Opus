# -*- coding: utf-8 -*-

"""
Contains RabbitMQ Consumer class
Use under MIT License
"""

__author__ = 'G_T_Y'
__license__ = 'MIT'
__version__ = '1.0.0'


import json
import threading
import pika
import logging

from . import settings
from .exceptions import RabbitmqConnectionError
from .actions import actions
from .publisher import Publisher
from .utils import format_response


class Consumer:
    """Used to consume message of request queue"""

    def __init__(self):
        self._host = settings.RABBITMQ_HOST
        self._vhost = settings.RABBITMQ_VHOST
        self._username = settings.RABBITMQ_USERNAME
        self._password = settings.RABBITMQ_PASSWORD
        self._port = settings.RABBITMQ_PORT
        self._request_queue = settings.REQUEST_QUEUE
        self.connection = None
        self.channel = None

    def connect(self):
        """Establish connection to rabbitmq server using parameters set by init function
        It update values of connection and channel parameters
        """

        if settings.DEBUG:
            parameters = pika.ConnectionParameters(self._host)
        else:
            credentials = pika.PlainCredentials(
                username=settings.RABBITMQ_USERNAME,
                password=settings.RABBITMQ_PASSWORD
            )
            parameters = pika.ConnectionParameters(
                host=self._host,
                port=self._port,
                virtual_host=self._vhost,
                credentials=credentials
            )

        try:
            msg = "Connection established successfully with rabbitmq server !!!"
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            print(msg)
            logging.info(msg)
        except Exception as e:
            raise RabbitmqConnectionError(str(e))

    @staticmethod
    def on_message(channel, method_frame, header_frame, body):
        """ Method called when a message is receive on request queue
        convert message to dictionary and launch handler function
        :param channel:
        :param method_frame:
        :param header_frame:
        :param body:
        """
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        publisher = Publisher()

        message = body.decode("utf8")
        print(message)
        logging.info(message)

        response = format_response(code="ERR400", status="error", message="", files_ids=[], action="")

        try:
            data = json.loads(message)
            action = data["action"]
            if action in actions:
                threading.Thread(target=actions[action], args=(data, )).start()
            else:
                response["action"] = action
                response["message"] = "This action does not exist on server."
                publisher.send_message(json.dumps(response))

        except json.JSONDecodeError:
            response["code"] = "ERR500"
            response["message"] = error = "Invalid JSON file"
            print(error)
            publisher.send_message(json.dumps(response))

    def run(self):
        """
        Start consuming messages on request queue
        :return:
        """
        self.channel.queue_declare(self._request_queue)
        self.channel.basic_consume(self._request_queue, self.on_message)
        try:
            msg = "Waiting for message ..."
            print(msg)
            logging.info(msg)
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.channel.stop_consuming()

        self.connection.close()
