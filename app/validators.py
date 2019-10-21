from jsonschema import validate, ValidationError


def validate_compare_input(message):
    """
    validate input for function that compare two songs

    :param message: message received by microservice
    :type message: `dict`
    :return: tuple with status and error message
    :rtype: `tuple`
    """
    input_schema = {
        "type": "object",
        "required": ["action", "song_1", "song_2"],
        "properties": {
            "action": {"type": "string", "description": "Function to call"},
            "song_1": {
                "type": "object",
                "required": ["file_id", "name", "content", "extension"],
                "properties": {
                    "name": {"type": "string"},
                    "file_id": {"type": "string", "description": "file_id as saved in a database"},
                    "content": {"type": "string", "description": "file converted to base64"},
                    "extension": {"type": "string"}
                }
            },
            "song_2": {
                "type": "object",
                "required": ["file_id", "name", "content", "extension"],
                "properties": {
                    "name": {"type": "string"},
                    "file_id": {"type": "string", "description": "file_id as saved in a database"},
                    "content": {"type": "string", "description": "file converted to base64"},
                    "extension": {"type": "string"}
                }
            }
        }
    }

    status = False
    error = ""
    try:
        status = validate(message, input_schema)
    except ValidationError as e:
        error = "Validation Error: " + str(e)

    return status, error


def validate_fingerprint_input(message):
    """
    Validate input for function that generate fingerprint of a song
    :param message:
    :return:
    :rtype: `tuple`
    """
    input_schema = {
        "type": "object",
        "required": ["action", "file_id", "song"],
        "properties": {
            "action": {"type": "string", "description": "Function to call"},
            "song": {
                "type": "object",
                "required": ["file_id", "name", "content", "extension"],
                "properties": {
                    "name": {"type": "string"},
                    "file_id": {"type": "string", "description": "file_id as saved in a database"},
                    "content": {"type": "string", "description": "file converted to base64"},
                    "extension": {"type": "string"}
                }
            }
        }
    }

    status = False
    error = ""
    try:
        status = validate(message, input_schema)
    except ValidationError as e:
        error = "Validation Error: " + str(e)

    return status, error
