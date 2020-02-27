from flask import Blueprint, render_template , request ,redirect , flash, url_for , session , escape
from werkzeug.security import generate_password_hash , check_password_hash
from models import *
from models.user import User
from models import user as u
users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')

@users_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('users/login.html')    


@users_blueprint.route('/', methods=['POST'])
def create():
    name = request.form.get("name")
    password = request.form.get("password")
    username = request.form.get("username")
    email = request.form.get("email")
    v = User(name = name, password=password, username =username, email = email)
    if v.save():
        flash("User successfully created.")
        return redirect(url_for('users.new'))
    else:
        return render_template('users/new.html', errors = v.errors)

# authenticate users
@users_blueprint.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    email_to_check = request.form.get("email")
    password_to_check = request.form.get("password")
    # find = User.get(User.email == email_to_check)
    test = User.get_or_none(User.email == email_to_check)
    #Check user name exist
   
    if test:
        login_user = User.get(User.email == email_to_check)
        hashed_password = login_user.password
        #Check password whether correct
        result = check_password_hash(hashed_password,password_to_check)
        if result:
            # breakpoint()
            session['username'] = login_user.email
            session_username = escape(session['username'])
            flash(f"Welcome back ,{login_user.name}")
            return render_template('/home.html')
        else:
            flash("Incorrect Email or Password") 
    else:
        flash("Email Does Not Exist")    
        
    return render_template('users/login.html')  


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
