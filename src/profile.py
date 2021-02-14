from flask import Blueprint
from flask_login import current_user, login_required
from src.models import User
from . import db


profile = Blueprint('profile', __name__)


@profile.route('/<name>/rating')
def rating(name):
  '''
  Returns the Users's rating 
  :param name: name of the user
  '''
  user = User.query.filter_by(name=name).first()
  if user:
    return str(user.rating)
  else:
    return f"{name} doesn\'t exisit"
  

