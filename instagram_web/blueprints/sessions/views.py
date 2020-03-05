from flask import Blueprint, render_template , request ,redirect,session , flash, url_for
from models.user import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash , check_password_hash
from instagram_web.util.google_oauth import oauth
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
            flash(f"Welcome back , {user.name}")
            # return render_template(url_for('users.show',id=user.id))
            return redirect(url_for('users.show',id=user.id))
        else:
            flash("Incorrect Email or Password") 
    else:
        flash("Email Does Not Exist")       
          
    return render_template('/sessions/new.html') 
    


@sessions_blueprint.route('/logout', methods=["GET"])
@login_required
def logout():
   logout_user()
   flash("Successfully logged out. Goodbye!")
   return redirect(url_for("home"))

#login with google
@sessions_blueprint.route('/google_login', methods=['GET'])
def google_login():
    redirect_uri = url_for('sessions.authorize', _external = True)
    return oauth.google.authorize_redirect(redirect_uri)


@sessions_blueprint.route('/authorize/google', methods=['GET'])
def authorize():
    oauth.google.authorize_access_token()
    email = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
    user = User.get_or_none(User.email == email)
    if user:
        login_user(user)
        return redirect(url_for('users.show', id = user.id))
    else:
        flash('Your google email is not registered in our system')
        return render_template('sessions/new.html')


@sessions_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
