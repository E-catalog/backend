from typing import Any
from flask import jsonify


Places = dict[str, Any]

class PlacesRepo:

    def __init__(self) -> None:
        self.last_id = 3
        self.pl_storage = {
            1: {"id": 1, "title":"Мамаев Курган", "category": "Курган"},
            2: {"id": 2, "title":"Красный Курган", "category": "Курган"},
            3: {"id": 3, "title":"Синий Курган", "category": "Курган"}
            }


    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id


    def get_all(self) -> Any:
        all_places = list(self.pl_storage.values())
        return jsonify(all_places)


    def get_by_id(self, uid: int) -> Any:
        return self.pl_storage[uid]


    def add(self, places: any) -> Any:
        new_uid = self.next_id()
        places['id'] = new_uid
        self.pl_storage[new_uid] = places
        return self.pl_storage[new_uid], 201


    def update(self, uid: int, places: any) ->Any:
        updating_places = self.pl_storage[uid]
        updating_places['title'] = places['title']
        updating_places['category'] = places['category']
        return updating_places


    def delete(self, uid: int) -> None:
        del self.pl_storage[uid]
        return {}, 204
