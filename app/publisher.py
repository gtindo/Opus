# -*- coding: utf-8 -*-

"""
Contains RabbitMQ Consumer class
Use under MIT License
"""

__author__ = 'G_T_Y'
__license__ = 'MIT'
__version__ = '1.0.0'


import pika

from . import settings
from .exceptions import RabbitmqConnectionError


class Publisher:
    """Used to publish messages on response queue"""

    def __init__(self):
        self._host = settings.RABBITMQ_HOST
        self._vhost = settings.RABBITMQ_VHOST
        self._port = settings.RABBITMQ_PORT
        self._username = settings.RABBITMQ_USERNAME
        self._password = settings.RABBITMQ_PASSWORD
        self._response_queue = settings.RESPONSE_QUEUE
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
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
        except Exception as e:
            raise RabbitmqConnectionError(str(e))

    def send_message(self, message):
        """Send message to response queue

        :param message: message to send
        :type message: `str`
        :return:
        """
        self.connect()
        self.channel.queue_declare(self._response_queue)
        self.channel.basic_publish(
            '',
            self._response_queue,
            message,
            pika.BasicProperties(
                content_type='application/json',
                delivery_mode=1
            )
        )
        self.connection.close()
