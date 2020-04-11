from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import mapper
from flask_sqlalchemy import SQLAlchemy
from services.database import metadata, db_session
import datetime
import random
import string

db = SQLAlchemy()

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

class StudentToProject(object):
	query = db_session.query_property()

	def __init__(self, project_id, user_id):
		self.project_id = project_id
		self.user_id = user_id
 
	def __repr__(self):
		return '<StudentToProject %r->%r>' % (self.user_id, self.project_id)

student_to_projects = Table('students_to_projects', metadata,
	Column('id', Integer(), primary_key=True),
	Column('project_id', String(80), ForeignKey('projects.project_id')),
	Column('user_id', String(80), ForeignKey('users.id')),
	db.UniqueConstraint('project_id', 'user_id', name='Index 3'),
	extend_existing=True
)
mapper(StudentToProject, student_to_projects)