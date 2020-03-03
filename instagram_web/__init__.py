from app import app
from flask import render_template, flash
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_login import login_user , LoginManager , current_user
from models.user import User
assets = Environment(app)
assets.register(bundles)
login_manager = LoginManager()
login_manager.init_app(app)

# login_manager.login_view = "users.show,id=3"
# login_manager.login_message ="What The Hell"
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
app.register_blueprint(sessions_blueprint, url_prefix="/donation")
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def not_authorized(e):
    return render_template('401.html'), 404

@app.route("/")
def home():
    
    return render_template('sessions/new.html')
    
    # return render_template('home.html')

@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id==user_id)


"""
@app.route('/signin', methods = ['GET','POST'])
def signin():
    email_to_check = request.form.get("email")
    password_to_check = request.form.get("password")

    #Check user name exist
    user_exist = u.User.get_or_none(u.User.email == email_to_check)
    if user_exist:
        login_user = u.User.get(u.User.email==email_to_check)
        hashed_password = login_user.password
        #Check password whether correct
        result = check_password_hash(hashed_password,password_to_check)
        if result:
            session['username'] = login_user.email
            return redirect(url_for('users'))
        else:
            flash("Incorrect Email or Password") 
    else:
        flash("Email Does Not Exist")    
        

    return redirect(url_for('user_login'))
"""