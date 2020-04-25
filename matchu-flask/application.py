from flask import Flask, Response, redirect, url_for, request, abort, render_template, session, jsonify, make_response
from functools import wraps, update_wrapper
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import string
import random
import json
import datetime

# This for encryption of differnt things
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Add the SQLAlchemy models
from services.database import init_db, db_session, Base
from models.user import User
from models.project import Project
from models.group import Group
from models.student_to_group import StudentToGroup
from models.student_to_project import StudentToProject
# from flask_dance.contrib.google import make_google_blueprint, google
# from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage

# Anonymous class for flask_login
from classes.anonymous import Anonymous

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:2020MATCHu!@matchuinstance.cfxzlncqju3l.us-east-1.rds.amazonaws.com:3306/matchu"


# -------------------------------------- #
#           Random Generators            #
# -------------------------------------- #
def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

def randomLetters(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters
	return ''.join(random.choice(letters) for i in range(stringLength))

# -------------------------------------- #
#            Flask_Login Init            #
# -------------------------------------- #
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.session_protection = "strong"
login_manager.anonymous_user = Anonymous
login_manager.init_app(application)


debug = True

# When the application is turned off
@application.teardown_appcontext
def shutdown_session(exception=None):
	db_session.close()



application.config["SECRET_KEY"] = 'adsfasdfasdfsdfasdfasdfqtdhfdfgadfgsdfgdsfgdf235235523512345asdfasdfasdfwqerwqer'
def nocache(view):
	@wraps(view)
	def no_cache(*args, **kwargs):
		response = make_response(view(*args, **kwargs))
		response.headers['Last-Modified'] = datetime.datetime.now()
		response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
		response.headers['Pragma'] = 'no-cache'
		response.headers['Expires'] = '-1'
		return response
		
	return update_wrapper(no_cache, view)

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

@application.route('/register', methods=["POST"])
def register():
	username = request.form['username']
	email = request.form['email']
	password = generate_password_hash(request.form['password'])
	id = randomString(50) if not 'uid' in request.form else request.form['uid']
	user_type = request.form['user_type']
	activation_token = randomString(50)

	userObject = User.query.filter_by(email=email).first()
	username_exists = User.query.filter_by(username=username).count()
	

	if userObject is None:
		if username_exists:
			return redirect(url_for('login', error="There's already someone with that username registered."))

		schedule = {}
		if user_type == "student":
			days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
			
			for day in days:
				if not request.form['{}_start'.format(day)] == "" and not request.form['{}_end'.format(day)] == "":
					start_time = datetime.datetime.strptime(request.form['{}_start'.format(day)], "%I:%M %p")
					end_time = datetime.datetime.strptime(request.form['{}_end'.format(day)], "%I:%M %p")

					if start_time.time() < end_time.time():
						if (end_time - start_time) > datetime.timedelta(hours=2):
							schedule[day] = [start_time.strftime("%H:%M"), end_time.strftime("%H:%M")]
						else:
							return redirect(url_for('login', error="Please ensure you choose a duration of at least 3 hours."))
					else:
						return redirect(url_for('login', error="There was an issue processing the schedule you provided. Please try again."))

			if len(schedule.keys()) < 3:
				return redirect(url_for('login', error="Please ensure you choose at least 3 days to meet."))

		user = User(username=username, password=password, email=email, id=id, user_type=user_type, activation_token=activation_token, schedule=schedule)
	else:
		return redirect(url_for('login', error="There's already someone with that email registered."))
		# userObject.username = username
		# userObject.password = password
		# userObject.uid = id
		# userObject.activation_token = activation_token
		# userObject.
		# user = userObject
	try:
		db_session.add(user)
		db_session.commit()
		login_user(user)
	except Exception as e:
		print(e)
		return redirect(url_for('login', error="There was an issue signing you up"))

	
	return redirect(url_for("projects", macro_id=None))

# somewhere to login
@application.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		registered_user = User.query.filter_by(email=email).first()
        
		if registered_user is None:
			return render_template('login.html', error="That didn't work.")

		if not registered_user.check_password(password):
			return render_template('login.html', error = "That didn't work.")

		# session.add(registered_user)
		# session.commit()

		if registered_user.is_authenticated():
			login_user(registered_user, remember=True)
			# current_user = reload_user(registered_user.id)
			return redirect(url_for("projects"))
		
	elif request.method == "GET":
		error = request.args.get('error', default = None, type = str)
		if not error == None:
			return render_template('login.html', error = error)

		# if not current_user.is_anonymous():
		#   current_user.check_login()
		
		if current_user.is_authenticated():
			return redirect(url_for("projects"))
		
	return render_template('login.html')

# somewhere to logout
@application.route("/logout")
@login_required
def logout():
	logout_user()
	return redirect("login")

# callback to reload the user object        
@login_manager.user_loader
def reload_user(userid):
	u = User.query.filter_by(id=userid).first()
	if not u is None:
		return u
	else:
		return 

@login_required
@application.route("/getProject")
def getProject():
	project_id = request.args.get('project_id', default = None, type = str)
	project = Project.query.filter_by(project_id=project_id).first()

	return jsonify({"name": project.project_name, "desc": project.description})

# @login_required
# @application.route("/editProject")
# def editProject():
# 	project_id = request.args.get('project_id', default = None, type = str)
# 	project = Project.query.filter_by(project_id=project_id).first()

# 	project.project_name = request.form['project_name']
# 	project.description = request.form['desc']

# 	try:
# 		db_session.add(project)
# 		db_session.commit()
# 	except:
# 		db_session.rollback()
# 		return redirect(url_for("projects", error="Something went wrong, try again a little later."))
# 	else:
# 		return redirect(url_for("projects", success="That project was successfully edited."))


@login_required
@nocache
@application.route("/project/<project_id>")
def project(project_id):
	error = request.args.get('error', default = None, type = str)
	success = request.args.get('success', default = None, type = str)

	if current_user.is_part_of_project(project_id):
		project = Project.query.filter_by(project_id=project_id).first()

		groups = project.get_groups()
		if not error == None:
			return render_template('project.html', project=project, error = error)

		if not success == None:
			return render_template('project.html', project=project)


		return render_template("project.html", project=project)
	else:
		return render_template("my-projects.html", error="You don't have access to this project.")


@login_required
@nocache
@application.route("/assignAutoAssign/<project_id>")
def assignAutoAssign(project_id):
	project = Project.query.filter_by(project_id=project_id).first()

	if current_user.id == project.user_id:
		result = project.assign_autoassign()
		if result:
			return redirect(url_for("project", project_id=project.project_id, success="Students were succesfully auto-assigned"))
		else:
			return redirect(url_for("project", project_id=project.project_id, error="There was an issue auto assigning groups"))
		

@login_required
@application.route("/joinGroup/<group_id>", methods=['POST', 'GET'])
def joinGroup(group_id):
	group = Group.query.filter_by(id=group_id).first()

	project = group.get_project()

	if current_user.user_type == "student":
		current_group = StudentToGroup.query.filter_by(user_id=current_user.id, group_id=group_id).first()
		print(current_group )
		if current_group == None:
			student_group = StudentToGroup.query.filter_by(user_id=current_user.id, project_id=project.project_id).first()

			if student_group is None:
				student_to_group = StudentToGroup(group_id, current_user.id)
				try:
					db_session.add(student_to_group)
					db_session.commit()
				except:
					db_session.rollback()
					return redirect(url_for("project", project_id=project.project_id, error="Something went wrong, try again a little later."))
				else:
					return redirect(url_for("project",  project_id=project.project_id, success="You were successfully added to that group."))
			else:
				return redirect(url_for("project", project_id=project.project_id, error="You are already registered for the group '" + student_group.get_group().name + "'"))
		else:
			return redirect(url_for("project", project_id=project.project_id, error="You are already part of this group."))
	else:
		return redirect(url_for("project", project_id=project.project_id, error="Only Students can join groups."))

@login_required
@application.route("/leaveGroup/<group_id>", methods=['POST', 'GET'])
def leaveGroup(group_id):
	group = Group.query.filter_by(id=group_id).first()

	project = group.get_project()

	if current_user.user_type == "student":
		current_group = StudentToGroup.query.filter_by(user_id=current_user.id, group_id=group_id).first()
		if current_group == None:
			return redirect(url_for("project", project_id=project.project_id, error="You are not part of '%s'" % (group.name)))
		else:
			try:
				db_session.delete(current_group)
				db_session.commit()
			except:
				 return redirect(url_for("project", project_id=project.project_id, error="Something went wrong, try again a little later."))

			return redirect(url_for("project", project_id=project.project_id, success="You were removed from '%s'" % (group.name)))
	else:
		return redirect(url_for("project", project_id=project.project_id, error="Only Students can join groups."))

@login_required
@application.route("/createGroup/<project_id>", methods=["POST"])
def createGroup(project_id):
	group_name = request.form['group_name']
	desc = request.form['desc']

	group = Group(group_name=group_name, project_id=project_id, solution_desc=desc)

	try:
		db_session.add(group)
		db_session.commit()
	except:
		return url_for("project", project_id=project_id, error="Something went wrong, try again a little later.")
	else:
		return url_for("project",  project_id=project_id, success="That group was successfully created.")

@application.route('/api/deleteGroup/<group_id>', methods=["GET"])
def deleteGroup(group_id):
	group = Group.query.filter_by(id=group_id).first()
	project_id = group.get_project().project_id

	try:
		db_session.delete(group)
		db_session.commit()
	except:
		return redirect(url_for("project", project_id=project_id, error="Something went wrong, try again a little later."))
	else:
		return redirect(url_for("project", project_id=project_id, success="That group was successfully deleted."))


@login_required
@application.route("/projects")
def projects():
	if current_user.is_anonymous() == True:
		return redirect(url_for("login", error="You need to be logged in to do that."))
	if current_user.user_type == "student":
		return render_template("my-projects.html", projects=current_user.get_projects())
	elif current_user.user_type == "teacher":
		return render_template("my-projects.html", projects=current_user.get_projects())

@application.route('/api/registerForProject', methods=["POST"])
def registerForProject():
	project_id = request.form['project_id']
	
	proj = Project.query.filter_by(nice_url=project_id).first()
	
	
	if not current_user.is_part_of_project(proj.project_id):
		stud_to_proj = StudentToProject(proj.project_id, current_user.id)

		try:
			db_session.add(stud_to_proj)
			db_session.commit()
		except:
			return url_for("projects", error="There was an error adding your to that project.")
		else:
			return url_for("projects", success="You were successfully added.")
	else:
		return url_for("projects", success="You are already part of this project.")

@application.route('/api/createProject', methods=["POST"])
def createProject():
	project_name = request.form['project_name']
	desc = request.form['desc']


	project = Project(project_name=project_name, user_id=current_user.id, description=desc)
	
	auto_assign_group = Group("Auto-Assign Group", project.project_id, "This is a group that will auto assign you to the group with the best schedule")
	project.autoAssign_group_id = auto_assign_group.id

	try:
		db_session.add(project)
		db_session.add(auto_assign_group)
		db_session.commit()

		if debug:
			all_students = User.query.filter_by(user_type="student").all()
			for student in all_students:
				stud_to_proj = StudentToProject(project.project_id, student.id)
				stud_to_aass = StudentToGroup(group_id=auto_assign_group.id, user_id=student.id)

				try:
					db_session.add(stud_to_proj)
					db_session.add(stud_to_aass)
					db_session.commit()
				except:
					continue
	except:
		return url_for("projects", error="Something went wrong, try again a little later.")
	else:
		return url_for("project", project_id=project.project_id, success="That project was successfully created.")
		
@application.route('/api/editProject', methods=["POST"])
def editProject():
	project_id = request.form['project_id']
	
	proj = Project.query.filter_by(project_id=project_id).first()
	
	proj.project_name = request.form['project_name']
	proj.description = request.form['desc']
	
	try:
		db_session.commit()
	except:
		return url_for("projects", error="Something went wrong, try again a little later.")
	else:
		return url_for("projects", success="That project was successfully edited.")

@application.route('/api/leaveProject', methods=["POST"])
def leaveProject():
	project_id = request.form['project_id']
	user_id = current_user.id

	print(project_id)

	if current_user.is_part_of_project(project_id):
		connection = StudentToProject.query.filter_by(project_id=project_id, user_id=user_id).first()
	else:
		return url_for("projects", error="You are not enrolled in that project.")

	db_session.delete(connection)
	db_session.commit()

	try:
		db_session.delete(connection)
		db_session.commit()
	except:
		return jsonify(False)
	else:
		return url_for("projects", success="You were successfully unenrolled.")



@application.route('/api/deleteProject', methods=["POST"])
def deleteProject():
	project_id = request.form['project_id']

	project = Project.query.filter_by(project_id=project_id).first()

	try:
		db_session.delete(project)
		db_session.commit()
	except:
		return jsonify(False)
	else:
		return url_for("projects", success="That project was successfully deleted.")




# some protected url
@application.route('/')
@nocache
def home():
	return render_template("index.html")

if __name__ == "__main__":
	application.run(host="127.0.0.1", port=5000,debug=True)
