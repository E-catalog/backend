from backend.database.db import db_session
from backend.database.models.individuals import Places


class PlacesRepo:


    def get_all(self):
        return db_session.query(Places).all()

    def get_by_id(self, id: int):
        return db_session.query(Places).get(id)    #заменить на id?

    def add(self, places) -> dict[str, str,]:
        new_places = places(
            name =places.name,
            id =places.id,
            head_of_excavations =places.head_of_excavations,
            type_of_burial_site =places.type_of_burial_site,
            coordinates = places.coordinates,
            comments = places.commments,
        )
        db_session.add(new_places)
        db_session.commit()
        return {
            'message': 'Новое место раскопок успешно создано',
        }


    def update(self, id: int, update) -> dict[str, str]:
        places = db_session.query(Places).get(id)

        places.name = update.name
        places.id = update.id
        places.head_of_excavations = update.head_of_excavations
        places.type_of_burial_site = update.type_of_burial_site
        places.coordinates = update.coordinates
        places.comments = update.commments

        db_session.commit()
        return{
            'message': 'Данные места раскопок успешно обновлены'
        }

    def delete(self, id: int) -> dict[str, str]:
        del self.pl_storage[id]
        return {
            'message': f'Место раскопок {id} удалено из базы данных'
        }
