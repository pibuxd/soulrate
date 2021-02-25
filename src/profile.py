from flask import Blueprint, json, render_template
from flask_login import current_user, login_required

from src.models import User
from src.rating.utils import change_rating

from . import db

profile = Blueprint('profile', __name__)


@login_required
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
    return render_template("profile.html", username=username, rating=rating)
  else:
    return f"<b>{name}</b> doesn\'t exisits"
  
  
@login_required
@profile.route('/<name>/uprate')
def uprate(name:str):
  '''
  Uprate the User's rating (increase)
  :param name: the User's name
  '''
  uprated = change_rating(name, 1)
  if uprated:
    print(f"log: {name} uprated")
    return json.dumps({"did":1})
  else:
    print(f"log: {name} didn\'t uprated")
    return json.dumps({"did":0})
  
  
@login_required
@profile.route('/<name>/downrate')
def downrate(name:str):
  '''
  Downrate the User's rating (decrease)
  :param name: the User's name
  '''
  downrated = change_rating(name, -1)
  if downrated:
    print(f"log: {name} downrated")
    return json.dumps({"did":1})
  else:
    print(f"log: {name} didn\'t downrated")
    return json.dumps({"did":0})
