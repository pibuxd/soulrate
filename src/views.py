from flask import Blueprint
from flask_login import current_user, login_required

views = Blueprint('views', __name__)

@views.route('/')
def home():
  if current_user.is_authenticated:
    return "hi user"
  else:
    return "hi guest"
  

@views.route('/rate')
@login_required
def rate():
  return 'jd'
