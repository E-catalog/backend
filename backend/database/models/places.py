from sqlalchemy import Column, Integer, String, Text
from backend.database.db import Base


class Places(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    head_of_excavations = Column(String)
    type_of_burial_site = Column(String)
    coordinates = Column(String)
    comments = Column(Text)


    def __repr__(self):
        return f'Индвид: индекс в базе {self.id}, {self.place}, {self.name}, {self.sex}, {self.age}'
