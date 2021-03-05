from flask import Blueprint, json
from flask_login import login_required

from src.models import User
from src.rating.utils import change_rating

from .. import db

rating = Blueprint('rating', __name__)


@login_required
@rating.route('/uprate/<name>')
def uprate(name:str):
  '''
  Uprate the User's rating (increase)
  :param name: the User's name
  :return json{"did":bool}: if 1 -> uprated, if 0 -> nothing
  '''
  uprated = change_rating(name, 1)
  if uprated:
    print(f"log: {name} uprated")
    return json.dumps({"did":1})
  else:
    print(f"log: {name} didn\'t uprated")
    return json.dumps({"did":0})
  
  
@login_required
@rating.route('/downrate/<name>')
def downrate(name:str):
  '''
  Downrate the User's rating (decrease)
  :param name: the User's name
  :return json{"did":bool}: if 1 -> downrated, if 0 -> nothing
  '''
  downrated = change_rating(name, -1)
  if downrated:
    print(f"log: {name} downrated")
    return json.dumps({"did":1})
  else:
    print(f"log: {name} didn\'t downrated")
    return json.dumps({"did":0})
  

@login_required
@rating.route('/rating/<name>')
def rating_of(name:str):
  '''
  Return the User's rating (decrease)
  :param name: the User's name
  :return json{"rating":int}: the User's rating
  '''
  user = User.query.filter_by(name=name).first()
  rating = user.rating
  
  return json.dumps({"rating":rating})