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

class Group(object):
	query = db_session.query_property()

	def __init__(self,  project_name, user_id, solution_desc):
		self.project_id = db.relationship('projects')
		self.name = name
		self.user_id = user_id
		self.solution_desc = solution_desc
 
	def __repr__(self):
		return '<Group %r>' % (self.username)

groups = Table('groups', metadata,
	Column('id', String(5), primary_key=True),
	Column('project_id', String(80)),
	Column('name', String(100)),
	Column('solution_desc', Text()),

	extend_existing=True
)
mapper(Group, groups)