import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


db_url = os.environ['DB_URL']
#db_url = 'postgresql://xfbywbjk:MtATDLV8hWG7-WVXi5vocRGscoqPWHY2@abul.db.elephantsql.com/xfbywbjk'
engine = create_engine(db_url)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
