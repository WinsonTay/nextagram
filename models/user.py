from models.base_model import BaseModel
# from models.follower_following import FollowerFollowing
from werkzeug.security import generate_password_hash ,check_password_hash
from flask_login import UserMixin,current_user
from playhouse.hybrid import hybrid_property, hybrid_method

import peewee as pw
import re

class User(BaseModel, UserMixin):
    name = pw.CharField(unique=False)
    password =pw.CharField()
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True, null=False)
    profile_image = pw.CharField(null=True)
    private = pw.BooleanField(default=False)

    @hybrid_property
    def profile_image_url(self):
        #if user had not uploaded an image
        if (self.profile_image == None): 
            return "https://nextagram-winson.s3.amazonaws.com/avatar/profile_img1.png"
        else:
            return f"https://nextagram-winson.s3.amazonaws.com/{self.profile_image}"
    @hybrid_method
    def is_following(self,user):
        from models.follower_following import FollowerFollowing
        check_following = FollowerFollowing.get_or_none((FollowerFollowing.fan_id == current_user.id) & (FollowerFollowing.idol_id == user.id))
        if check_following == None:
            return False
        else:
            return True

   
    """
    @hybrid_method
    def is_following(self,user):
        check_following =FollowerFollowing.get_or_none(FollowerFollowing.idol_id == user.id and FollowerFollowing.fan_id == self.id)
        if check_following == None:
            return False
        else:
            return True 
    """
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

class Story(BaseModel, UserMixin):
    user = pw.ForeignKeyField(User, backref='stories')
    story_image = pw.CharField(null=True)
    msg = pw.TextField(null=True)
    
    def validate(self):
        pass

    @hybrid_property
    def story_image_url(self):
        return f"https://nextagram-winson.s3.amazonaws.com/{self.story_image}"
    


def pwd_formatcheck(pw):
    patterns = [ r"[A-Z]{1}", r"[a-z]{1}" , r"\W"]
    for pattern in patterns:
     match = re.search(pattern,pw)
     if match == None:
        return False      
    else:
        return True

