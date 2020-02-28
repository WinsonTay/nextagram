from flask import Blueprint, render_template , request ,redirect,session , flash, url_for
from models.user import User
from flask_login import login_user, logout_user


from werkzeug.security import generate_password_hash , check_password_hash
sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')


@sessions_blueprint.route('/', methods=['GET'])
def new():
    return render_template('/sessions/new.html')

@sessions_blueprint.route('/new', methods=['GET','POST'])
def login():
    email_to_check = request.form.get("email")
    password_to_check = request.form.get("password")
    # find = User.get(User.email == email_to_check)
    user_exist = User.get_or_none(User.email == email_to_check)
    #Check user name exist
   
    if user_exist:
        user = User.get(User.email == email_to_check)
        hashed_password = user.password
        #Check password whether correct
        result = check_password_hash(hashed_password,password_to_check)
        if result:
            # breakpoint()
            # session['username'] = login_user.email
            login_user(user)
            flash(f"Welcome back ,{user.name}")
            return render_template('/home.html')
        else:
            flash("Incorrect Email or Password") 
    else:
        flash("Email Does Not Exist")       
          
    return render_template('/sessions/new.html')
    


@sessions_blueprint.route('/logout', methods=["GET"])
def logout(username):
    pass

@sessions_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@sessions_blueprint.route('/new', methods=["GET"])
def login2():
    return "USERS"


@sessions_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@sessions_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
