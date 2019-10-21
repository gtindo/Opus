"""
All project settings

:APP_NAME: Name of application
:APP_VERSION: Application version
:BASE_DIR: full path of project directory
:DEBUG: Turn dev or production status
:RABBITMQ_HOST: hostname for rabbitmq
:RABBITMQ_VHOST: virtual host name
:RABBITMQ_PORT: rabbitmq port
:RABBITMQ_USERNAME: rabbitmq username
:RABBITMQ_PASSWORD: rabbitmq password
:REQUEST_QUEUE: queue used to listen on message reception
:RESPONSE_QUEUE: queue used to publish messages
"""

import os
import configparser

# project directory path
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

parser = configparser.ConfigParser()
parser.read(os.path.join(BASE_DIR, "config.txt"))

# Warning !! Don't use in production with debug turned to true
if parser["MODE"]["DEBUG"] == "True":
    DEBUG = True
else:
    DEBUG = False

rabbitmq = parser["RABBITMQ"]

# Rabbitmq connection parameters
RABBITMQ_HOST = rabbitmq["HOST"]
RABBITMQ_VHOST = rabbitmq["VIRTUAL_HOST"]
RABBITMQ_USERNAME = rabbitmq["USERNAME"]
RABBITMQ_PASSWORD = rabbitmq["PASSWORD"]
RABBITMQ_PORT = int(rabbitmq["PORT"])

# Request and response queues
REQUEST_QUEUE = rabbitmq["REQUEST_QUEUE"]
RESPONSE_QUEUE = rabbitmq["RESPONSE_QUEUE"]

# App params
app = parser["APP"]
APP_NAME = app["APP_NAME"]
APP_VERSION = app["APP_VERSION"]

# Directory for input files
INPUTS_DIR = os.path.join(BASE_DIR, "app/data/inputs")

# Directory for output files
OUTPUTS_DIR = os.path.join(BASE_DIR, "app/data/outputs")

try:
    os.mkdir(INPUTS_DIR)
    os.mkdir(OUTPUTS_DIR)
except OSError:
    pass

AUTHORIZED_EXTENSIONS = [
    "mp3",
    "ogg",
    "flac",
    "wav",
    "acc"
]

