from flask import Flask, Response, redirect, url_for, request, abort, render_template, session, jsonify, make_response
from functools import wraps, update_wrapper
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import string
import random
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

# from flask_dance.contrib.google import make_google_blueprint, google
# from flask_dance.consumer.storage.sqla import OAuthConsumerMixin, SQLAlchemyStorage

# Anonymous class for flask_login
from classes.anonymous import Anonymous

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/matchu"


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
login_manager.init_app(app)


# When the app is turned off
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()



app.config["SECRET_KEY"] = 'adsfasdfasdfsdfasdfasdfqtdhfdfgadfgsdfgdsfgdf235235523512345asdfasdfasdfwqerwqer'
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

@app.route('/register', methods=["POST"])
def register():
    username = request.form['username']
    email = request.form['email']
    password = generate_password_hash(request.form['password'])
    id = randomString(50) if not 'uid' in request.form else request.form['uid']
    activation_token = randomString(50)

    userObject = User.query.filter_by(email=email).first()
    
    if userObject is None:
        user = User(username=username, password=password, email=email, id=id, activation_token=activation_token)
    else:
        userObject.username = username
        userObject.password = password
        userObject.uid = id
        userObject.activation_token = activation_token
        user = userObject

    try:
        db_session.add(user)
        db_session.commit()
        login_user(user)
    except:
        return jsonify(False)
    else:
        return redirect(url_for("projects", macro_id=None))

# somewhere to login
@app.route("/login", methods=["GET", "POST"])
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
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("login")

# callback to reload the user object        
@login_manager.user_loader
def reload_user(userid):
    u = User.query.filter_by(id=userid).first()
    if not u is None:
        return User(u.username, u.password, u.email, id=userid)
    else:
        return 

@login_required
@app.route("/projects")
def projects():
    if current_user.user_type == "student":
        return render_template("my-projects.html", current_user=current_user)
    elif current_user.user_type == "teacher":
        pass

@app.route('/api/createProject', methods=["POST"])
def createProject():
    project_name = request.form['project_name']
    desc = request.form['desc']


    project = Project(project_name=project_name, creator=current_user.id, description=desc)
    
    try:
        db_session.add(project)
        db_session.commit()
    except:
        return url_for("projects", error="Something went wrong, try again a little later.")
    else:
        return url_for("projects", success="That project was successfully created.")

@app.route('/api/deleteProject', methods=["POST"])
def deleteProject():
    project_id = request.form['project_id']

    project = Project.query.filter_by(project_id=project_id).first()
    project_name = macro.macro_name
    

    try:
        db_session.delete(project)
        db_session.commit()
    except:
        return jsonify(False)
    else:
        return url_for("macros", success="That project was successfully deleted.")




# some protected url
@app.route('/')
@nocache
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000,debug=True)
