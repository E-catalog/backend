from sqlalchemy import Column, Integer, String, Text
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


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
