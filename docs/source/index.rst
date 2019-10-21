.. Micro Service documentation master file, created by
   sphinx-quickstart on Thu Sep 12 10:24:37 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Configuration of Project Environment
************************************
Micro service 1.0.0

Overview on How to Run this Project
===================================
1. Create a Python virtual environment
2. Install required packages
3. A running RabbitMQ Server

Setup procedure
===============
1. Create a Python Virtual Environment
    - Install virtualenv::

        sudo pip install virtualenv

    - Create virtualenv::

        virtualenv -p python3 <name of virtualenv>

    - Install requirements::

        pip install -r requirements.txt

2. Create configuration file
    - Create file (using config.example.txt as template)

        cd app && and touch config.txt

    - Write configurations on file
         :[RABBITMQ]:
         :HOST: host_name
         :VIRTUAL_HOST: virtual_host
         :USERNAME: username
         :PASSWORD: password
         :PORT: port
         :REQUEST_QUEUE: request_queue_name
         :RESPONSE_QUEUE: response_queue_name
         :[MODE]:
         :DEBUG: True or False
         :[APP]:
         :APP_NAME: Name of application
         :APP_VERSION: Version of application

3. Set DEBUG variable in app/settings.py
    - For development : DEBUG = True
    - For production : DEBUG = False

4. Run main.py::

    python -m app.main

    or

    ./start.sh

Run unit tests
=================
    cd tests
    python -m unittest


Documentation for the Code
**************************
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   consumer
   exceptions
   handler
   logger
   publisher
   settings
   validators

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

