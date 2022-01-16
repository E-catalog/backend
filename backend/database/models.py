from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.database.session import Base


class Places(Base):
    __tablename__ = 'places'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    head_of_excavations = Column(String)
    type_of_burial_site = Column(String)
    coordinates = Column(String)
    comments = Column(Text)
    individuals = relationship('Individuals', lazy='joined', back_populates='places')

    def __repr__(self):
        return f'Место: индекс в базе {self.id}, {self.place}'


class Individuals(Base):
    __tablename__ = 'individuals'

    uid = Column(Integer, primary_key=True)
    place_uid = Column(Integer, ForeignKey(Places.uid), nullable=False)
    name = Column(String, nullable=False)
    year_of_excavation = Column(Integer)
    individual_type = Column(String)
    sex = Column(String)
    age = Column(String)
    preservation = Column(String)
    epoch = Column(String)
    comments = Column(Text)
    places = relationship('Places', lazy='joined', back_populates='individuals')

    def __repr__(self):
        return 'Индвид: индекс [{uid}], {place}, {name}, {sex}, {age}'.format(
            uid=self.id,
            place=self.place,
            name=self.name,
            sex=self.sex,
            age=self.age,
        )
