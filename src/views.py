from flask import Blueprint, render_template, flash
from flask_login import current_user, login_required
from src.models import User
from . import db


views = Blueprint('views', __name__)


@views.route('/')
def home():
  text = "hi guest"
  
  if current_user.is_authenticated:
    text = "hi user"
    
  return text
  