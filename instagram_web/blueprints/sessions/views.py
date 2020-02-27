from flask import Blueprint, render_template , request ,redirect , flash, url_for
from models.user import User

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')


@sessions_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('login.html')



@sessions_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@sessions_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@sessions_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@sessions_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
