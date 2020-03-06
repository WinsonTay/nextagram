from models.base_model import BaseModel
from models.user import User
from flask_login import current_user
import peewee as pw
from playhouse.hybrid import hybrid_property , hybrid_method


class FollowerFollowing(BaseModel):
    fan_id  = pw.ForeignKeyField(User, backref="fans")
    idol_id = pw.ForeignKeyField(User, backref="idols")
    approved = pw.BooleanField(default=False)

    def validate(self):
        pass
    
