from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class user(Base):
  __tablename__ = 'Users'
  id = Column(Integer, primary_key=True)
  Email = Column(String)
  Password = Column(String)
  j