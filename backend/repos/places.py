from backend.database.models.places import Places
from backend.database.session import db_session


class PlacesRepo:

    def get_all(self) -> list[Places]:
        return db_session.query(Places).all()

    def get_by_id(self, uid: int):
        return db_session.query(Places).get(uid)

    def add(self, places) -> Places:
        new_places = Places(
            name=places.name,
            head_of_excavations=places.head_of_excavations,
            type_of_burial_site=places.type_of_burial_site,
            coordinates=places.coordinates,
            comments=places.comments,
        )
        db_session.add(new_places)
        db_session.commit()
        return new_places

    def update(self, id: int, update) -> Places:
        place = db_session.query(Places).get(id)

        place.name = update.name
        place.id = update.id
        place.head_of_excavations = update.head_of_excavations
        place.type_of_burial_site = update.type_of_burial_site
        place.coordinates = update.coordinates
        place.comments = update.commments

        db_session.commit()
        return place

    def delete(self, id: int) -> None:
        individual = db_session.query(Places).get(id)
        db_session.delete(individual)
        db_session.commit()
