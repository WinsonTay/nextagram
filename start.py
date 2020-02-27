"""
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash , check_password_hash
from app import app
from flask import Flask, render_template, url_for, request ,redirect , flash,session, escape
from models import user as u
import instagram_api
import instagram_web

csrf = CSRFProtect(app)
@app.route('/')
def users():
    print('testing')
    logged_user = escape(session['username'])
    if 'username' in session:
        flash(f"Hello there {logged_user}")
    
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
"""

from app import app
import instagram_api
import instagram_web

if __name__ == '__main__':
    app.run()
