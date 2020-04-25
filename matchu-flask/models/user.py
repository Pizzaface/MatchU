from sqlalchemy import Table, Column, Integer, String, Text
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
import json

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

class User(object):
	query = db_session.query_property()

	def __init__(self , email, username=None, password=None, activation_token=None, schedule={}, id=None, user_type="student"):
		if not id == None:
			self.id = id
		else:
			self.id = randomString(50)

		self.username = username
		self.password = password
		self.email = email
		self.is_anonymous = False
		
		self.user_type = user_type

		self.schedule = json.dumps(schedule)
		self.activation_token = activation_token

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def is_part_of_project(self, project_id):
		if self.user_type == "teacher":
			check = Project.query.filter_by(user_id=self.id, project_id=project_id).count()
		elif self.user_type == "student":
			check = StudentToProject.query.filter_by(user_id=self.id, project_id=project_id).count()

		print(check)
		if check == 1:
			return True
		else:
			return False

	def get_projects(self):
		if self.user_type == "teacher":
			self.projects = Project.query.filter_by(user_id=self.id).all()
		elif self.user_type == "student":
			projects = []
			links = StudentToProject.query.filter_by(user_id=self.id).all()
			for project in links:
				projects.append(Project.query.filter_by(project_id=project.project_id).first())

			self.projects = projects

		return self.projects

	def is_authenticated(self):
		return True

	def is_active(self):
		return True
 
	def is_anonymous(self):
		return False
 
	def get_id(self):
		return self.id

	def refresh(self):
		self = self.query.filter_by(id=self.id)
		return self
 
	def __repr__(self):
		return '<User %r>' % (self.username)

users = Table('users', metadata,
	Column('username', String(80), unique=True , index=True, nullable=True),
	Column('password' , Text(), nullable=True),
	Column('user_type', String(20)),
	Column('id',String(50),unique=True , primary_key=True),
	Column('email',String(120),unique=True , index=True),
	Column('schedule', Text()),
	Column('activation_token',String(90),unique=True, nullable=True),
	extend_existing=True
)
mapper(User, users)

from .student_to_project import StudentToProject
from .project import Project