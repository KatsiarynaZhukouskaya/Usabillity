from peewee import *


db = SqliteDatabase('database.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    description = CharField()
   
    class Meta:
        database = db

class January(BaseModel):
    pass

class February(BaseModel):
    pass

class March(BaseModel):
    pass

class April(BaseModel):
    pass

class May(BaseModel):
    pass

class June(BaseModel):
    pass

class July(BaseModel):
    pass

class August(BaseModel):
    pass

class September(BaseModel):
    pass

class October(BaseModel):
    pass

class November(BaseModel):
    pass

class December(BaseModel):
    pass