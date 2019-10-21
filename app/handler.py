import os
import json
from . import utils
from .settings import AUTHORIZED_EXTENSIONS
from .publisher import Publisher


def fingerprint_handler(message):
    publisher = Publisher()
    action = message["action"]
    file_string = message["song"]["content"]
    file_id = message["song"]["file_id"]
    file_extension = message["song"]["extension"]

    response = utils.format_response(code="SUC200", status="success", message={}, files_ids=[file_id], action=action)

    if file_extension in AUTHORIZED_EXTENSIONS:
        saved_file = utils.save_file(file_string, file_id, file_extension)
        data = utils.generate_fingerprint(saved_file)

        response["message"] = data

        publisher.send_message(json.dumps(response))

        os.remove(saved_file)
    else:
        response["code"] = "ERR401"
        response["status"] = "error"
        response["message"] = 'The extension of file is not allowed.'

        publisher.send_message(json.dumps(response))


def compare_handler(message):
    publisher = Publisher()
    action = message["action"]

    file_1_string = message["song_1"]["content"]
    file_1_id = message["song_1"]["file_id"]
    file_1_extension = message["song_1"]["extension"]

    file_2_string = message["song_2"]["content"]
    file_2_id = message["song_2"]["file_id"]
    file_2_extension = message["song_2"]["extension"]

    response = utils.format_response(
        code="SUC200",
        status="success",
        message={},
        files_ids=[file_1_id, file_2_id],
        action=action
    )

    if file_1_extension in AUTHORIZED_EXTENSIONS and file_2_extension in AUTHORIZED_EXTENSIONS:
        saved_file_1 = utils.save_file(file_1_string, file_1_id, file_1_extension)
        saved_file_2 = utils.save_file(file_2_string, file_2_id, file_2_extension)

        data = utils.compare_files(saved_file_1, saved_file_2)
        response["message"] = data

        publisher.send_message(json.dumps(response))

        os.remove(saved_file_1)
        os.remove(saved_file_2)
    else:
        response["code"] = "ERR401"
        response["status"] = "error"
        response["message"] = 'The extension of file is not allowed.'

        publisher.send_message(json.dumps(response))
