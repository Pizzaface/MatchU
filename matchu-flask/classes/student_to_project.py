from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
import random
from services.database import Base
from sqlalchemy.orm import relationship


class StudentToProject(Base):
	__tablename__ = "student_to_projects" 
	id = Column('id', Integer())
	project_id = Column(Integer, ForeignKey('projects.id'))
	student_id = Column(Integer, ForeignKey('users.id'))

	def __init__(self, project_id, student_id):
		self.project_id = project_id
		self.student_id = student_id

 
	def __repr__(self):
		return '<StudentToProject %r>' % (self.username)