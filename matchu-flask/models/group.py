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

class Group(object):
	query = db_session.query_property()

	def __init__(self,  group_name, project_id, solution_desc):
		self.id = randomString(5)
		self.project_id = project_id
		self.name = group_name
		self.solution_desc = solution_desc
 
	def has_member(self, user_id):
		return StudentToGroup.query.filter_by(group_id=self.id, user_id=user_id).first() is not None

	def get_project(self):
		return Project.query.filter_by(project_id=self.project_id).first()
		
	def __repr__(self):
		return '<Group %r>' % (self.name)

groups = Table('groups', metadata,
	Column('id', String(5), primary_key=True),
	Column('project_id', String(80), ForeignKey('projects.project_id')),
	Column('name', String(100)),
	Column('solution_desc', Text()),

	extend_existing=True
)
mapper(Group, groups)

from .project import Project
from .student_to_group import StudentToGroup