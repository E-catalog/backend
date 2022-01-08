from sqlalchemy import Column, Integer, String, Text
from backend.database.db import Base


class Individuals(Base):
    __tablename__ = 'individuals'

    id = Column(Integer, primary_key=True)
    place = Column(String)
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
