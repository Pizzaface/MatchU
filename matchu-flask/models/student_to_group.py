from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapper
from services.database import metadata, db_session
import datetime
import random
import string

"""def randomString(stringLength=10):
	Generate a random string of fixed length 
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))"""
	
def randomInteger(intLength=10):
	"""Generate a random int of fixed length"""
	return random.randint(1,intLength)

class StudentToGroup(object):
	query = db_session.query_property()

	def __init__(self, group_id, user_id):
		self.id = randomInteger(25)
		self.group_id = group_id
		self.user_id = user_id
		self.project_id = self.get_group().get_project().project_id
		self.project = Project.query.filter_by(project_id=self.project_id)


	def get_group(self):
		return Group.query.filter_by(id=self.group_id).first()

	def get_user(self):
		return User.query.filter_by(id=self.user_id).first()

	def __repr__(self):
		return '<StudentToGroup %r->%r>' % (self.group_id, self.user_id	)

student_to_groups = Table('student_to_groups', metadata,
	Column('id', Integer, primary_key=True),
	Column('user_id', String(80), ForeignKey('users.id')),
	Column('group_id', String(80), ForeignKey('groups.id')),
	Column('project_id', String(80), ForeignKey('projects.project_id')),
	#Column('user_id', String(80), ForeignKey('users.id')),

	extend_existing=True
)
mapper(StudentToGroup, student_to_groups)

from .group import Group
from .user import User
from .project import Project