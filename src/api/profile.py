from flask import Blueprint, Response, json
from src.models import User

from .. import db

profile = Blueprint('profile', __name__)


@profile.route('/<name>')
def info(name:str):
  '''
  Returns info about the User
  :param name: The User's name
  '''
  user = User.query.filter_by(name=name).first()
  
  if user:
    username = user.name
    rating = user.rating
    return json.dumps({"username":username, "rating":rating})
  else:
    return Response(status=404) # doesn't exists
