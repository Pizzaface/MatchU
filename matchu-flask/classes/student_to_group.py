from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
import random
from services.database import Base
from sqlalchemy.orm import relationship


class StudentToGroup(Base):
	__tablename__ = "student_to_groups" 
	id = Column('id', Integer())
	group_id = Column(Integer, ForeignKey('groups.id'))
	student_id = Column(Integer, ForeignKey('users.id'))

	def __init__(self, group_id, student_id):
		self.group_id = group_id
		self.student_id = student_id

 
	def __repr__(self):
		return '<StudentToGroup %r->%r>' % (self.group_id, self.student_id)