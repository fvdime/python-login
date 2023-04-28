from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #sqlalchemy automaticly add date for us
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #foreign key a column in our database table that refers column of another database
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 


#we are saying the database to all users should look like this
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')