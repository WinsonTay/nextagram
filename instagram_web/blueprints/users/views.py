from flask import Blueprint, render_template , request ,redirect , flash, url_for , session , escape , Flask
from werkzeug.security import generate_password_hash , check_password_hash
from werkzeug.utils import secure_filename
from instagram_web.util.s3_uploader import upload_file_to_s3
# from models import *
from flask_login import login_user, logout_user, login_required , current_user
from models.user import User, Story
# from models import user as u
users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')
"""
@users_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('users/login.html')    
"""


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

@users_blueprint.route('/<id>', methods=["GET"])
def show(id):
    userinfo = User.get_by_id(id)
    
    return render_template('users/index.html', userinfo=userinfo)
"""
@users_blueprint.route('/', methods=["GET"]
def index():
    return render_template('/index.html')
"""

@users_blueprint.route('/<id>/edit', methods=["GET"])
@login_required
def edit(id):
    userinfo = User.get_by_id(id)
    return render_template('users/edit.html', userinfo=userinfo)

@users_blueprint.route('/feed', methods=["GET"])
@login_required
def feed():
    users = User.select().where(id != current_user.id)
    return render_template('users/newsfeed.html',users = users)

@users_blueprint.route('/<id>/update', methods=['POST'])
@login_required
def update(id):
    user = User.get_by_id(id)
    update_msg = []
    if current_user.id == user.id: # Check whether current editing user is edit the own profile, if not Block authorization
        new_username = request.form.get("username")
        new_email = request.form.get("email")
        if new_username != user.username:
            user.username = new_username
            if user.save():
                update_msg.append(f"Update new user name to {new_username}")
            else:
                for msg in user.errors:
                 flash(msg)
                return redirect(url_for("users.show",id=id))
        if new_email != user.email:
            user.email  = new_email
            if user.save():
                update_msg.append(f"Update new email to {new_email}")
            else:
                for msg in user.errors:
                 flash(msg)
                return redirect(url_for("users.show",id=id))

        for success_msg in update_msg:
            flash(success_msg)
        return redirect(url_for('users.show', id = id))
    else:
        flash("You are not authorized to do this")
        return redirect(url_for('users.show', id = id))

@users_blueprint.route('/<id>/upload_file', methods=['POST'])
@login_required
def upload_file(id):
    # user_file = request.form.get("user_file")
    # breakpoint()
    editing_user = User.get_by_id(id)
    #check Authentication
    if current_user.id != editing_user.id:
        flash("You are not authorized to do this")
        return redirect(url_for('users.show',id=current_user.id))
    if "user_file" not in request.files:
        flash ("No File Found")
        return redirect(url_for('users.edit', id = id))
    file = request.files["user_file"]
   

    if file.filename == "":
        flash("Please Select a file")
        return redirect(url_for('users.edit', id = id))
    
    file.filename = secure_filename(file.filename)

    if not upload_file_to_s3(file):
        flash("Opps, Something wrong with the Uploading")
        return redirect(url_for('users.edit', id = id))

    #else succeded upload file to AMAZON S3
    editing_user.profile_image = file.filename
    editing_user.save()
    flash("Uploaded file succeed")
    # return redirect(url_for('users.edit', id = id))

    return redirect(url_for('users.edit', id = id))

@users_blueprint.route('/<id>/story', methods=['GET','POST'])
@login_required
def story(id):
    # userstory = User.get_by_id(id)
    return render_template('/users/story.html',userid=id)

@users_blueprint.route('<id>/story_post', methods=['POST'])
@login_required
def story_post(id):
    upload_user = User.get_by_id(id)
    # story_file = request.form.get('story_file')
    message = request.form.get('message')
    if current_user.id != upload_user.id:
        flash("You are not Authorized to Do this")
        return render_template('/users/story.html',id = current_user.id)
    
    if 'story_file' not in request.files:
        flash ("No File Found")
        return redirect(url_for('users.story', id = current_user.id))

    file = request.files['story_file']
    if file.filename == "":
        flash("Please Select a file")
        return redirect(url_for('users.story', id = current_user.id))
    
    file.filename = secure_filename(file.filename)

    if not upload_file_to_s3(file):
        flash("Opps, Something wrong with the Uploading")
        return redirect(url_for('users.story', id = current_user.id))
    
    new_story = Story(msg=message,story_image = file.filename, user=upload_user)
    new_story.save()
    flash("You Just Posted a new Story")
    return redirect(url_for('users.show', id = id))



    