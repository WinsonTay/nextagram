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

@app.route('/login')
def user_login():
    return render_template('login.html')


@app.route('/new', methods = ['POST'])
def createnew():
    name = request.form.get("name")
    password = request.form.get("password")
    username = request.form.get("username")
    email = request.form.get("email")
    u = user.User(name = name, password=password, username =username, email = email)
    if u.save():
        flash("User successfully created.")
        return redirect(url_for('user_signup'))
    else:
        return render_template('sign_up.html', errors = u.errors)
@app.route('/signin', methods = ['POST'])
def signin():
    email = request.form.get("email")
    password = request.form.get("password")
    login_user = user.User.select(email,password)

  

if __name__ == '__main__':
    app.run()
