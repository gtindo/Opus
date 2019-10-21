from .consumer import Consumer
from . import settings

print("""
============= {} {} Started =============
""".format(settings.APP_NAME, settings.APP_VERSION))


def main():
    consumer = Consumer()
    consumer.connect()
    consumer.run()


main()
