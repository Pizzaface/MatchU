from flask_sqlalchemy import SQLAlchemy
import timeago
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
import random
from services.database import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
import json

class User(Base):
	__tablename__ = "users" 
	username = Column('username', String(80), unique=True , index=True, nullable=True)
	password = Column('password' , Text(), nullable=True)
	user_type = Column('user_type', String(20))
	id = Column('id',String(50),unique=True , primary_key=True)
	email = Column('email',String(120),unique=True , index=True)
	schedule = Column('schedule', Text())
	activation_token = Column('activation_token',String(90),unique=True, nullable=True)

	def __init__(self , email, username=None, password=None, activation_token=None, schedule={}, id=None, user_type="student"):
		if not id == None:
			self.id = id
		else:
			self.id = randomString(50)

		self.username = username
		self.password = password
		self.email = email
		self.projects = relationship('projects')
		self.user_type = user_type
		self.schedule = json.dumps(schedule)
		self.activation_token = activation_token
		
	def check_password(self, password):
		return check_password_hash(self.password, password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return self.id
 
	def __repr__(self):
		return '<User %r>' % (self.username)