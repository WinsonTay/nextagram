import peewee as pw
from models.base_model import BaseModel
from models.user import Story, User

class Donation(BaseModel):
    amount = pw.DecimalField()
    image = pw.ForeignKeyField(Story,backref="donations")
    user = pw.ForeignKeyField(User, backref="donations")

    def validate(self):
        pass
    
    