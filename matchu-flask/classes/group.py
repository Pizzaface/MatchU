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

	def __init__(self,  project_name, user_id, solution_desc):
		self.project_id = db.relationship('projects')
		self.name = name
		self.user_id = user_id
		self.solution_desc = solution_desc
 
	def __repr__(self):
		return '<Group %r>' % (self.username)