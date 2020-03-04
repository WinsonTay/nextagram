from app import app
from flask import render_template, flash
from instagram_web.blueprints.users.views import users_blueprint
from instagram_web.blueprints.sessions.views import sessions_blueprint
from instagram_web.blueprints.donation.views import donation_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from flask_login import login_user , LoginManager , current_user
from models.user import User
from instagram_web.util.google_oauth import oauth
assets = Environment(app)
assets.register(bundles)
#Login manager init
login_manager = LoginManager()
login_manager.init_app(app)
#Google authorization init


# login_manager.login_view = "users.show,id=3"
# login_manager.login_message ="What The Hell"
app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")
app.register_blueprint(donation_blueprint, url_prefix="/donation")

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
