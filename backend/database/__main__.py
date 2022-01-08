from backend.database.db import Base, engine
from backend.database.models.individuals import Individuals
from backend.database.models.places import Places


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
