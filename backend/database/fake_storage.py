from typing import Any
from flask import jsonify


Individual = dict[str, Any]
places = dict[str, Any]


class IndividualsRepo:

    def __init__(self) -> None:
        self.last_id = 13
        self.storage = {
            11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
            12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
            13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
            }


    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id


    def get_all(self) -> list[Individual]:
        all_individuals = list(self.storage.values())
        return jsonify(all_individuals)


    def get_by_id(self, uid: int) -> Individual:
        return self.storage[uid]


    def add(self, individual: Individual) -> Individual:
        new_uid = self.next_id()
        individual['id'] = new_uid
        self.storage[new_uid] = individual
        return self.storage[new_uid], 201


    def update(self, uid: int, individual: Individual) -> Individual:
        updating_individual = self.storage[uid]
        updating_individual['title'] = individual['title']
        updating_individual['place'] = individual['place']
        return updating_individual


    def delete(self, uid: int) -> None:
        del self.storage[uid]
        return {}, 204



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
