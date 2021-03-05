from flask import Blueprint, Response, json, request
from flask_cors import cross_origin
from src.models import User
from src.rating.utils import change_rating

from .. import db

rating = Blueprint('rating', __name__)


@rating.route('/uprate/<name>')
@cross_origin()
def uprate(name:str):
  '''
  Uprate the User's rating (increase)
  :param name: the User's name
  '''
  token = request.cookies.get("token")
  
  if token: # !LOGGED
    uprated = change_rating(name, 1, token=token)
  else:
    return Response(status=401) # unauthorized
  
  user = User.query.filter_by(token=token).first()
  
  if not user:
    return Response(status=404) # doesn't exists
  
  if uprated:
    print(f"log: {name} uprated")
    return Response(status=201) # success
  else:
    print(f"log: {name} didn\'t uprated")
    return Response(status=409) # already uprated
  
  
@rating.route('/downrate/<name>')
@cross_origin()
def downrate(name:str):
  '''
  Downrate the User's rating (decrease)
  :param name: the User's name
  '''
  token = request.cookies.get("token")
  
  if token: # !LOGGED:
    downrated = change_rating(name, -1, token=token)
  else:
    return Response(status=401) # unauthorized
  
  user = User.query.filter_by(name=name).first()
  
  if not user:
    return Response(status=404) # doesn't exists
  
  if downrated:
    print(f"log: {name} downrated")
    return Response(status=201) # success
  else:
    print(f"log: {name} didn\'t downrated")
    return Response(status=409) # already uprated
  

@rating.route('/rating/<name>')
@cross_origin()
def rating_of(name:str):
  '''
  Return the User's rating (decrease)
  :param name: the User's name
  :return json{"rating":int}: the User's rating
  '''
  user = User.query.filter_by(name=name).first()
  
  if not user:
    return Response(status=404) # doesn't exists
  
  rating = user.rating
  
  return json.dumps({"rating":rating})
