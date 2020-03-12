from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapper
from services.database import metadata, db_session
import datetime
import random
import string

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

class Project(object):
	query = db_session.query_property()

	def __init__(self,  project_name, creator, description):
		self.project_id = randomString(50)
		self.project_name = project_name
		self.creator = creator
		self.description = description
 
	def __repr__(self):
		return '<Project %r>' % (self.username)

projects = Table('projects', metadata,
	Column('project_id', String(80), primary_key=True, unique=True , index=True),
	Column('project_name', String(100)),
	Column('creator', String(80), ForeignKey("users.id")),
	Column('description', Text()),

	extend_existing=True
)
mapper(Project, projects)