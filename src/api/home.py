from flask import Blueprint, Response, json
from flask_login import current_user, login_required
from src.models import User

from .. import db

views = Blueprint('views', __name__)


@views.route('/home')
def home():
  if not current_user.is_authenticated:
    return json.dumps({"username": "guest"})
    
  username = current_user.name
  rating = current_user.rating
  
  names = []
  
  for name in User.query.all():
    names.append(name.name)
  
  return json.dumps({"username":username, "rating":rating, "names":names})
