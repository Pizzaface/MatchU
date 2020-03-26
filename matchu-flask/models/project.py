from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapper, relationship
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

	def __init__(self,  project_name, user_id, description):
		self.project_id = randomString(50)
		self.project_name = project_name
		self.user_id = user_id
		self.description = description
		self.groups = get_groups()
		self.nice_url = self.project_id[:8]


	def get_groups(self):
		self.groups = Group.query.filter_by(project_id=self.project_id).all()

		return self.groups
 
	def __repr__(self):
		return '<Project %r>' % (self.project_name)

projects = Table('projects', metadata,
	Column('project_id', String(80), primary_key=True, unique=True , index=True),
	Column('project_name', String(100)),
	Column('user_id', String(80), ForeignKey("users.id")),
	Column('description', Text()),
	Column('nice_url', String(8)),
	extend_existing=True
)
mapper(Project, projects)

from .group import Group