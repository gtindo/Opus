import chromaprint
import acoustid
import os
import base64
from fuzzywuzzy import fuzz

from .settings import INPUTS_DIR


def format_response(**kwargs):
    """
    take response params and format with a dictionary
    :param kwargs:
    :return:
    :rtype: `dict`
    """

    response = {
        "status": kwargs["status"],
        "code": kwargs["code"],
        "message": kwargs["message"],
        "action": kwargs["action"],
        "files_ids": kwargs["files_ids"]
    }

    return response


def generate_fingerprint(file_path):
    """
    generate a song fingerprint given his location on filesystem
    :param file_path: file location
    :return: a dict with fingerprint and song duration
    :rtype: `dict`
    """
    duration, fp_encoded = acoustid.fingerprint_file(file_path)
    fingerprint, version = chromaprint.decode_fingerprint(fp_encoded)

    return {
        "fingerprint": fingerprint,
        "duration": duration
    }


def compare_files(file_1, file_2):
    """
    Compare fingerprint of 2 files an return a dict with comparison ration and files duration

    :param file_1: path of file_1
    :param file_2: path of file_2
    :return:
    :rtype: `dict`
    """
    duration_1, fingerprint_1 = generate_fingerprint(file_1)
    duration_2, fingerprint_2 = generate_fingerprint(file_2)

    ratio = fuzz.ratio(fingerprint_1, fingerprint_2)

    return {
        "ratio": ratio,
        "song_1_duration": duration_1,
        "song_2_duration": duration_2
    }


def save_file(file_string, file_id, extension):
    """
    Decode base64 file string an save result in app/data/input folder

    :param file_string:
    :param file_id:
    :param extension:
    :return:
    """
    content = base64.b64decode(file_string).decode("utf-8")
    file_name = file_id + "." + extension
    file_location = os.path.join(INPUTS_DIR, file_name)

    with open(file_location, "w") as f:
        f.write(content)

    return file_location
