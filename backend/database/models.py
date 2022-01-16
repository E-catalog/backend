from sqlalchemy import Column, Integer, String, Text

from backend.database.session import Base


class Individuals(Base):
    __tablename__ = 'individuals'

    id = Column(Integer, primary_key=True)
    place = Column(String, nullable=False)
    name = Column(String, nullable=False)
    year_of_excavation = Column(Integer)
    individual_type = Column(String)
    sex = Column(String)
    age = Column(String)
    preservation = Column(String)
    epoch = Column(String)
    comments = Column(Text)

    def __repr__(self):
        return 'Индвид: индекс [{uid}], {place}, {name}, {sex}, {age}'.format(
            uid=self.id,
            place=self.place,
            name=self.name,
            sex=self.sex,
            age=self.age,
        )


class Places(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    head_of_excavations = Column(String)
    type_of_burial_site = Column(String)
    coordinates = Column(String)
    comments = Column(Text)

    def __repr__(self):
        return f'Место: индекс в базе {self.id}, {self.place}'
