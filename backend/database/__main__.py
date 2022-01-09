from backend.database.session import Base, engine
from backend.database.models import *


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
