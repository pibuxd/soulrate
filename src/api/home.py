from flask import Blueprint, Response, json, request
from flask_cors import cross_origin
from src.models import User

from .. import db

views = Blueprint('views', __name__)


@views.route('/home')
@cross_origin()
def home():
  token = request.cookies.get("token")
  
  if not token: # !NOT LOGGED
    return json.dumps({"username": "guest"})
  
  token = request.cookies.get("token")
  print(token)
  user = User.query.filter_by(token=token).first()
  username = user.name
  rating = user.rating
  
  names = []
  
  for name in User.query.all():
    names.append(name.name)
  
  return json.dumps({"username":username, "rating":rating, "names":names})
