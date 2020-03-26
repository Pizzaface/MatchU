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

class StudentToGroup(object):
	query = db_session.query_property()

	def __init__(self, group_id, user_id):
		self.id = randomString(5)
		self.group_id = group_id
		self.user_id = user_id
 
	def __repr__(self):
		return '<StudentToGroup %r->%r>' % (self.group_id, self.user_id	)

student_to_groups = Table('student_to_groups', metadata,
	Column('id', String(5), primary_key=True),
	Column('group_id', String(80), ForeignKey('groups.id')),
	Column('user_id', String(80), ForeignKey('users.id')),

	extend_existing=True
)
mapper(StudentToGroup, student_to_groups)