from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(Email, Password):

	user_object = user(Email= Email, Password= Password)
	session.add(user_object)
	session.commit()
	



def add_product(name, price, picture, description):
	product_object = Product(
		name = name
		price = price 
		picture = picture
		description = description)
	product.add(product_object)
	session.commit()

add_product()
