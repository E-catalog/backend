from typing import Any
from flask import jsonify


places = dict[str, Any]
class PlacesRepo:

    def __init__(self) -> None:
        self.last_id = 3
        self.ztorage = {
        1: {"id": 1, "title":"Мамаев Курган", "category": "Курган"},
        2: {"id": 2, "title":"Красный Курган", "category": "Курган"},
        3: {"id": 3, "title":"Синий Курган", "category": "Курган"}
        }


    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id


    def get_all(self) -> list[places]:
        all_places = list(self.ztorage.values())
        return jsonify(all_places)


    def get_by_id(self, uid: int) -> places:
        return self.ztorage[uid]


    def add(self, places: places) -> places:
        new_uid = self.next_id()
        places['id'] = new_uid
        self.ztorage[new_uid] = places
        return self.ztorage[new_uid], 201


    def update(self, uid: int, places: places) -> places:
        updating_place = self.ztorage[uid]
        updating_place['title'] = places['title']
        updating_place['category'] = places['category']
        return updating_place


    def delete(self, uid: int) -> None:
        del self.ztorage[uid]
        return {}, 204

