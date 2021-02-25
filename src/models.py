from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
  '''
  Informations about the User
  '''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150), unique=True)
  password = db.Column(db.String(200))
  rating = db.Column(db.Integer, default=0)
  upvoted = db.Column(db.String(1000000), default="")
  downvoted = db.Column(db.String(1000000), default="")
  ip = db.Column(db.String(150))
  
  