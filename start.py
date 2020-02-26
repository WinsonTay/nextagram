from app import app
from flask import Flask, render_template, url_for, request ,redirect , flash
from models import user 
import instagram_api
import instagram_web

@app.route('/')
def users():
    return render_template('home.html')

@app.route('/sign_up')
def user_signup():
    return render_template('sign_up.html')


@app.route('/new' ,methods = ["POST"])
def createnew():
    name = request.form("")
    password = request.form("")
    username = request.form("")


    # u = user.User(name = name, password=password, username =username)
    # if u.save():
    #     flash("User successfully created.")
    #     return redirect(url_for('user_signup'))
    # else:
    #     return render_template('/sign_up')
    print(name,password,username)
    return redirect(url_for('user_signup'))

if __name__ == '__main__':
    app.run()
