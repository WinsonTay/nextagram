from flask import Blueprint, render_template , request ,redirect , flash, url_for , Flask
from werkzeug.security import generate_password_hash , check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required , current_user
from models.user import User, Story
# from models import user as u
donation_blueprint = Blueprint('donation',
                            __name__,
                            template_folder='templates')


@donation_blueprint.route('/<story_id>/new', methods=['GET'])
def new(story_id):
    image = Story.get_or_none(Story.id == story_id)
    if not image:
        flash("No Image found")


    return render_template('donation/new.html')