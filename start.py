from app import app
from flask import Flask, render_template, url_for, request ,redirect
import instagram_api
import instagram_web

@app.route('/')
def users():
    return render_template('home.html')

@app.route('/new')
def newuser():
    return render_template('newuser.html')


if __name__ == '__main__':
    app.run()
