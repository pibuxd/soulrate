from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from src.models import User

from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  '''
  Login user to service
  '''
  name = request.form.get('name', None)
  password = request.form.get('password', None)
  
  user = User.query.filter_by(name=name).first()
  
  if name == None:
    return render_template("login.html")
  
  if user:
    if check_password_hash(user.password, password):
      login_user(user, remember=True)
      print(f'log: account \"{name}\" logged')
      return redirect(url_for('views.home'))
    else:
      print(f'log: login \"{name}\" failed -> bad password')
  else:
    print(f'log: account \"{name}\" does\'t exist')
  
  return render_template("login.html")


@login_required
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
  '''
  Logout user from service
  '''
  if current_user.is_authenticated:
    logout_user()
  
  print('log: logged out')
  return redirect(url_for('views.home'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  '''
  Create new object user and login to service
  '''
  name = request.form.get('name', None)
  password = request.form.get('password', None)
  
  if name == None:
    return render_template("sign-up.html")
  
  ip = request.remote_addr

  new_user = User(
    name = name,
    password = generate_password_hash(password, method='sha256'),
    ip = ip
  )
  
  if bool(User.query.filter_by(name=name).first()):
    print(f'log: account \"{name}\" didn\'t created -> exists')
  else:
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)
    print(f'log: account \"{name}\" created')
  
  return render_template("sign-up.html")
