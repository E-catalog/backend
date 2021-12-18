from typing import Any
from flask import jsonify


Individual = dict[str, Any]

class IndividualsRepo:

    storage = {
    11: {"id": 11, "title": "Неопознанный объект #11", "place": "Мамаев курган"},
    12: {"id": 12, "title": "Неопознанный объект #12", "place": "Мамаев курган"},
    13: {"id": 13, "title": "Неопознанный объект #13", "place": "Мамаев курган"}
    }


    def get_all(self) -> list[Individual]:
        all_individuals = list(self.storage.values())
        return jsonify(all_individuals)


    def get_by_id(self, uid: int) -> Individual:
        return self.storage[uid]


    def add(self, individual: Individual) -> Individual:
        new_uid = max(self.storage) + 1
        self.storage[new_uid] = {
            "id": new_uid,
            "title": individual['title'],
            "place": individual['place']
            }
        return self.storage[new_uid], 201


    def update(self, uid: int, individual: Individual) -> Individual:
        updating_individual = self.storage[uid]
        updating_individual['title'] = individual['title']
        updating_individual['place'] = individual['place']
        return updating_individual


    def delete(self, uid: int) -> None:
        del self.storage[uid]
        return {}, 204
