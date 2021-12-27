from backend.database.db import Base, engine
from backend.database.individuals import Individuals


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
