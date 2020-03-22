from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapper
from services.database import metadata, db_session
import datetime
import random
import string

class StudentToProject(object):
	query = db_session.query_property()

	def __init__(self, user_id, description):
		self.project_id = randomString(50)
		self.user_id = user_id
 
	def __repr__(self):
		return '<Project %r>' % (self.username)

student_to_projects = Table('student_to_projects', metadata,
	Column('id', Integer(), primary_key=True),
	Column('project_id', String(80), ForeignKey('projects.id')),
	Column('user_id', String(80), ForeignKey('users.id')),

	extend_existing=True
)
mapper(StudentToProject, student_to_projects)