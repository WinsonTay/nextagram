from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    name = pw.CharField(unique=False)
    password =pw.CharField()
    username = pw.CharField(unique=True)
    email = pw.CharField(unique=True, null=False)
 
def validate():
     pass
