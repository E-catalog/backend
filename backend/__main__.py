from backend.app import app
from backend.config import config


def main():
    app.run(config.host, config.port)


if __name__ == '__main__':
    main()
