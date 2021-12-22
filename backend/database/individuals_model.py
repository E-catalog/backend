from typing import Text
from sqlalchemy import Column, Integer, String, Text, Date
from db import Base, engine


class SqlIndividualsRepo(Base):
    __tablename__ = 'individuals'

    id = Column(Integer, primary_key=True)
    place = Column(String) # from places
    name = Column(String)
    year_of_excavation = Column(Integer)
    individual_type = Column(String)
    sex = Column(String)
    age = Column(String)
    preservation = Column(String)
    epoch = Column(String)
    comments = Column(Text)

    def __repr__(self):
        return f'Индвид: индекс в базе {self.id}, {self.place}, {self.name}, {self.sex}, {self.age}'
