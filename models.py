from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, Boolean
db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)



class Pet(db.Model):
    '''Sets up the database for the Pet'''

    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

    name = db.Column(db.String(50), nullable=False, unique=False)
    
    species = db.Column(db.String(50), nullable=False, unique=False)

    photo_url = db.Column(db.String(150), nullable=True, unique=False)
    
    age = db.Column(db.Integer(), nullable=False, unique=False)
    
    notes = db.Column(db.String(500), nullable=False, unique=False)
    
    available = db.Column(db.Boolean(), default=True, nullable=False, unique=False)


