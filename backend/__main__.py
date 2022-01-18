import logging

from backend.app import app
from backend.config import config

logging.basicConfig(level=logging.DEBUG)


def main():
    app.run(host=config.host, port=config.port)


if __name__ == '__main__':
    main()
