from flask import Blueprint, Response, request
from flask_login import current_user, login_required, login_user, logout_user
from src.models import User
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  '''
  Login user
  '''
  name = request.form.get('name', None)
  password = request.form.get('password', None)
  
  user = User.query.filter_by(name=name).first()
  
  if user:
    if check_password_hash(user.password, password):
      login_user(user, remember=True)
      print(f'log: account \"{name}\" logged')
      return Response(status=201) # success
    else:
      print(f'log: login \"{name}\" failed -> bad password')
      return Response(status=401) # bad password
  else:
    print(f'log: account \"{name}\" does\'t exist')
    return Response(status=404) # bad username, doesn't exists
  


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
  '''
  Logout user
  '''
  if current_user.is_authenticated:
    logout_user()
    print('log: logged out')
    return Response(status=200) # success
  else:
    return Response(status=401) # unauthorized, not logged



@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  '''
  Create new object user and login to the service, sign up user
  '''
  name = request.form.get('name', None)
  password = request.form.get('password', None)
  
  if name == None:
    return Response(status=409) # already exists
  
  ip = request.remote_addr

  new_user = User(
    name = name,
    password = generate_password_hash(password, method='sha256'),
    ip = ip
  )
  
  if bool(User.query.filter_by(name=name).first()):
    print(f'log: account \"{name}\" didn\'t created -> exists')
    return Response(status=409) # already exists
  else:
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)
    print(f'log: account \"{name}\" created')
    return Response(status=201) # success
