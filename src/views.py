from flask import Blueprint, flash, render_template, json
from flask_login import current_user, login_required

from src.models import User

from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
  if not current_user.is_authenticated:
    return render_template("home.html", username="guest")
    
  username = current_user.name
  rating = current_user.rating
  
  names = []
  
  for name in User.query.all():
    names.append(name.name)
  
  return render_template("home.html", username=username, rating=rating, names=json.dumps(names))
  