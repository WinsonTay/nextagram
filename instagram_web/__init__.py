from app import app
from flask import render_template
from instagram_web.blueprints.users.views import users_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")

app.register_blueprint(users_blueprint, url_prefix="/sessions")
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')


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