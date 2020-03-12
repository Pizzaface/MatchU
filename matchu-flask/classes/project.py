from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
import random
from services.database import Base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


class Project(Base):
	__tablename__ = "projects" 
	id = Column('project_id', String(80), primary_key=True, unique=True , index=True)
	project_name = Column('project_name', String(100))
	creator = Column('creator', String(80), ForeignKey("users.id"))
	description = Column('description', Text())

	def __init__(self,  project_name, creator, description):
		self.project_id = randomString(50)
		self.project_name = project_name
		self.creator = creator
		self.description = description
 
	def __repr__(self):
		return '<Project %r>' % (self.username)