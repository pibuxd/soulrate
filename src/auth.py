from flask import Blueprint, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
  name = 'test'
  password = 'xd'
  
  user = User.query.filter_by(name=name).first()
  
  if user:
    if check_password_hash(user.password, password):
      login_user(user, remember=True)
      print(f'log: account \"{name}\" logged')
      return redirect(url_for('views.home'))
    else:
      print(f'log: login \"{name}\" failed -> bad password')
  else:
    print(f'log: account \"{name}\" does\'t exist')
  
  return "<p>Login</p>"


@auth.route('/logout')
def logout():
  if current_user.is_authenticated:
    logout_user()
  
  print('log: logged out')
  return redirect(url_for('views.home'))


@auth.route('/sign-up')
def sign_up():
  name = 'test22'
  password = 'xd'
  rating = 50
  
  new_user = User(name=name, password=generate_password_hash(password, method='sha256'), rating=rating)
  db.session.add(new_user)
  
  try:
    db.session.commit()
    login_user(new_user, remember=True)
    print(f'log: account \"{name}\" created')
    return redirect(url_for('views.home'))
  except:
    print(f'log: account \"{name}\" didn\'t created -> exists')
    
  
  return "<p>Sign up</p>"
