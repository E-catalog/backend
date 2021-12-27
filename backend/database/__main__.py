from backend.database.individuals_model import Individuals


def main():
    creator = Individuals()
    creator.create_table()


if __name__ == "__main__":
    main()
