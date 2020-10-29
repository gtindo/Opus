# Opus

Audio Fingerprinting microservice

## Overview on How to Run this Project

1. Install ffmpeg and on server
2. Create a Python virtual environment
3. Install required packages
4. A running RabbitMQ Server

# Setup procedure
1. Install ffmpeg
    ````shell script
    sudo apt-get install ffmpeg
2. Create a Python Virtual Environment
    - Install virtualenv
        ````shell script
        sudo pip install virtualenv

    - Create a virtualenv
        ````shell script
        virtualenv -p python3 <name of virtualenv>

    - Install requirements
        ````shell script
        pip install -r requirements.txt

3. Create configuration file
    - Create file (using config.example.txt as template)
       
       ````shell script
        cd app && and touch config.txt

    - Write configurations on file (like config.example.txt)\
         [RABBITMQ] \
         HOST = host_name \
         VIRTUAL_HOST = virtual_host \
         USERNAME = username \
         PASSWORD = password \
         PORT = port \
         REQUEST_QUEUE = request_queue_name \
         RESPONSE_QUEUE = response_queue_name \
         \
         [MODE] \
         DEBUG = True or False \
         \
         [APP] \
         APP_NAME = Name of application \
         APP_VERSION = Version of application \

4. Set DEBUG variable in app/settings.py
    - For development : DEBUG = True
    - For production : DEBUG = False

5. Run main.py
    ```shell script
    python -m app.main
   
    ./start.sh
   
## Run unit tests  
    cd tests
    python -m unittest


## Messages

### Compare two songs

* Input Message
```json
{
    "action": "compare",
    "song_1": {
      "name": "song_1",
      "file_id": "unique identifier of file",
      "content": "file encoded with base64",
      "extension": "mp3"  
    },
    "song_2": {
      "name": "song_2",
      "file_id": "unique identifier of file",
      "content": "file encoded with base64",
      "extension": "mp3"  
    }
}
```

* Output Message

```json
{
  "action": "compare",
  "code": "message code",
  "message": {
    "ratio": "ratio",
    "song_1_duration": "duration_1",
    "song_2_duration": "duration_2"
  },
  "status": "true or false",
  "files_ids": ["file1_id", "file2_id"]
}
```

### Generate fingerprint of a song

* Input Message

```json
{
  "action": "fingerprint",
  "song": {
    "name": "song",
    "file_id": "unique identifier",
    "content": "file encoded with base64",
    "extension": "mp3"
  }
}
```

* Output Message

```json
{
  "action": "fingerprint",
  "code": "message code",
  "message": {
    "fingerprint": "fingerprint",
    "duration": "duration"
  },
  "status": "true or false",
  "files_ids": ["file_id"]
}
```

## Author 

G_T_Y
