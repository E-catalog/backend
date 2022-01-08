from backend.app import app
from backend.config import config


def main():
    app.run(host=config.host, port=config.port)


if __name__ == '__main__':
    main()
