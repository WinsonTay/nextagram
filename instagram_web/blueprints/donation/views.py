from flask import Blueprint, render_template , request ,redirect , flash, url_for , Flask
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user, login_required , current_user
from models.user import User, Story
from models.donation import Donation
from instagram_web.util.bthelper import gateway

donation_blueprint = Blueprint('donation',
                            __name__,
                            template_folder='templates')

@donation_blueprint.route('<story_id>/new', methods=['GET'])
def new(story_id):
    image = Story.get_or_none(Story.id == story_id)
    if not image:
        flash("No Image found")
        return render_template(url_for('users.show' , id = current_user.id))
    client_token = gateway.client_token.generate()

    if not client_token:
        flash("No Token Found")
        return render_template(url_for('users.show',id = current_user.id))

    return render_template('donation/new.html' ,image=image,client_token=client_token)

@donation_blueprint.route('/<story_id>/create', methods = ["POST"])
@login_required
def create(story_id):
    nonce = request.form.get("payment_method_nonce")
    amount = int(request.form.get("amount"))
    if not nonce:
        flash("Invalid Credit card details","warning")
        return redirect(url_for('users.show',id = current_user.id))
    # Check again for image existence, User might delete photo while doing the transactions
    image = Story.get_or_none(Story.id == story_id)

    if not image:
        flash("The Image had been removed by User")
        return render_template(url_for('users.show',id = current_user.id))
 
    if amount <= 0:
        flash("No donation amount provided")
        return redirect(url_for('users.show',id=current_user.id))

    result = gateway.transaction.sale({
        "amount": amount,
        "payment_method_nonce": nonce,
        "options": {
        "submit_for_settlement": True
        }
    })
    if not result:
        flash("Sorry Dude, Payment Failed")
        return redirect(url_for('users.show',id=current_user.id))
    else:
        donate = Donation(amount=amount , image_id = story_id , user_id = current_user.id)
        if donate.save():
         flash(f"You just donate {amount}")
         return redirect(url_for('users.show',id = current_user.id))
        else:
         flash('Records Fail')
         return redirect(url_for('users.show',id = current_user.id))
    
    

  