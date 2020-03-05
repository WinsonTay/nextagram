from flask import Blueprint, render_template , request ,redirect,session , flash, url_for
from flask_login import current_user
from models.user import User
from models.follower_following import FollowerFollowing

follower_blueprint = Blueprint('follower_following',
                            __name__,
                            template_folder='templates')

@follower_blueprint.route('/<idol_id>', methods=['POST'])
def create(idol_id):
    new_idol = FollowerFollowing(fan_id = current_user.id, idol_id = idol_id)
    idol_info = User.get_by_id(idol_id)
    
    if new_idol.save():
        flash(f"You Just followed {idol_info.name}")
        return redirect(url_for('users.feed'))
    else:
        flash("Oops Something went wrong while following")
        return redirect(url_for('users.feed'))

@follower_blueprint.route('/<idol_id>/delete', methods=['POST'])
def delete(idol_id):
    idol = FollowerFollowing.get_or_none((FollowerFollowing.idol_id == idol_id) & (FollowerFollowing.fan_id == current_user.id))
    idol_info = User.get_by_id(idol_id)

    if idol.delete_instance():
        flash(f"You Just Unfollow {idol_info.name}")
    else:
        flash("Ops, Something Went Wrong.. ")

    return redirect(url_for('users.feed'))
    