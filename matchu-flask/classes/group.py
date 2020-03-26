from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
import random
from services.database import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


class Group(Base):
	__tablename__ = "groups" 
	id = Column('id', String(5), primary_key=True)
	project_id = Column('project_id', ForeignKey("projects.id"))
	description = Column('description', Text())

	def __init__(self,  group_name, project_id, solution_desc):
		self.id = randomString(5)
		self.project_id = project_id
		self.project = Project.query.filter_by(project_id=project_id).first()
		self.name = group_name
		self.solution_desc = solution_desc
 
	def __repr__(self):
		return '<Group %r>' % (self.username)