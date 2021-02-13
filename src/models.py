from src.app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(150))
  rating = db.Column(db.Integer)
  ip = db.Column(db.String(150))
  
  