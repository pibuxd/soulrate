from flask import Blueprint, json, render_template
from flask_login import current_user, login_required

from src.models import User

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