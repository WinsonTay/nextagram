from models.base_model import BaseModel
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_login import UserMixin,current_user

import peewee as pw
import re

class User(BaseModel, UserMixin):
    name = pw.CharField(unique=False)
    password =pw.CharField()
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True, null=False)
    def validate(self):
     if(current_user.is_authenticated) and (current_user.password == self.password):
        pass
     else:    
        if pwd_formatcheck(self.password) == False:
            self.errors.append("Password must be upper case or lower case and Special Characters")
        if len(self.password) <= 6:
            self.errors.append("Password must be more than 6 characters")
        else:
            self.password = generate_password_hash(self.password)
     
    #Check duplcation of user name
     if current_user.is_authenticated:
         if current_user.username != self.username:
            duplicate_usernames = User.get_or_none(User.username == self.username)
            if duplicate_usernames:
                self.errors.append("User name existed")
     else:
        duplicate_usernames = User.get_or_none(User.username == self.username)
        if duplicate_usernames:
            self.errors.append("User name existed")

    #Check Duplication of email
     if current_user.is_authenticated:
         if current_user.email != self.email:
            duplicate_emails = User.get_or_none(User.email == self.email)
            if duplicate_emails:
                 self.errors.append("Email already Registered")
     else:
        duplicate_emails = User.get_or_none(User.email == self.email)
        if duplicate_emails:
            self.errors.append("Email already Registered")

     # FLASK LOGIN CODE
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id  
"""
@login_manager.user_loader
def load_user(User.id):
  return User.get(User.id)
"""

def pwd_formatcheck(pw):
    patterns = [ r"[A-Z]{1}", r"[a-z]{1}" , r"\W"]
    for pattern in patterns:
     match = re.search(pattern,pw)
     if match == None:
        return False      
    else:
        return True

