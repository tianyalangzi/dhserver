# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://dhome:123456@localhost/dhomedb", encoding='utf-8')

Session = sessionmaker(bind=engine)
Base = declarative_base()

'''
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    age = Column(String(32), nullable=False)
    register_date = Column(Date, nullable=False)
    def __repr__(self):
        return '<%s name:%s>' % (self.id, self.name)
'''
class App(Base):
	__tablename__ = 'app01'
	id = Column(Integer,primary_key=True)
	name = Column(String(20), nullable=False)
	def __repr__(self):
		return '<%s name:%s>' % (self.id, self.name)


Base.metadata.create_all(engine)
