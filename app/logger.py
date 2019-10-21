import os
import logging

from . import settings

LOGS_PATH = os.path.join(settings.BASE_DIR, "logs")
LOGS_FILE = os.path.join(LOGS_PATH, "main.log")

try:
    os.mkdir(LOGS_PATH, 777)
except OSError:
    pass


logging.basicConfig(
    filename=LOGS_FILE,
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

LOGGER = logging.getLogger("APP")
