from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from services.database import metadata, db_session
from werkzeug.security import generate_password_hash, check_password_hash
from pytz import timezone
import pytz
import datetime
import timeago
import random
import string
from sqlalchemy.orm import relationship


def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

class User(object):
	query = db_session.query_property()

	def __init__(self , email, username=None,password=None, activation_token=None, id=None, user_type="student"):
		if not id == None:
			self.id = id
		else:
			self.id = randomString(50)

		self.username = username
		self.password = password
		self.email = email
		self.projects = relationship('projects')
		self.user_type = user_type
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

users = Table('users', metadata,
	Column('username', String(80), unique=True, index=True, nullable=True),
	Column('password', String(100), nullable=True),
	Column('id',String(50),unique=True, primary_key=True),
	Column('email',String(120),unique=True , index=True),
	Column('activation_token',String(90),unique=True, nullable=True),
	extend_existing=True
)
mapper(User, users)