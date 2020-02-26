from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash
from app import app
from flask import Flask, render_template, url_for, request ,redirect , flash
from models import user 
import instagram_api
import instagram_web

csrf = CSRFProtect(app)
@app.route('/')
def users():
    return render_template('home.html')

@app.route('/sign_up')
def user_signup():
    return render_template('sign_up.html')


@app.route('/new', methods = ['POST'])
def createnew():
    name = request.form.get("name")
    password = request.form.get("password")
    username = request.form.get("username")
    hash_password = generate_password_hash(password)
    email = request.form.get("email")

    u = user.User(name = name, password=hash_password, username =username, email = email)
    if u.save():
         flash("User successfully created.")
         return redirect(url_for('user_signup'))
    else:
      return render_template('/sign_up')
  

if __name__ == '__main__':
    app.run()
