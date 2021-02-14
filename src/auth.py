from flask import Blueprint, request, render_template
from flask_login import login_user, login_required, logout_user, current_user
from src.models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  '''
  Login user to service
  '''
  name = request.form.get('name', None)
  password = request.form.get('password', None)
  
  user = User.query.filter_by(name=name).first()
  
  if user:
    if check_password_hash(user.password, password):
      login_user(user, remember=True)
      print(f'log: account \"{name}\" logged')
      #return redirect(url_for('views.home'))
    else:
      print(f'log: login \"{name}\" failed -> bad password')
  else:
    print(f'log: account \"{name}\" does\'t exist')
  
  return render_template("login.html")


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
  '''
  Logout user from service
  '''
  if request.method == 'POST':
    if current_user.is_authenticated:
      logout_user()
    
    print('log: logged out')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  '''
  Create new object user and login to service
  '''
  if request.method == 'POST':
    name = request.form.get('name', None)
    password = request.form.get('password', None)
    
    rating = 50 # default
    ip = request.remote_addr

    new_user = User(
      name = name,
      password = generate_password_hash(password, method='sha256'),
      rating = rating,
      ip = ip
    )
    
    if bool(User.query.filter_by(name=name).first()):
      print(f'log: account \"{name}\" didn\'t created -> exists')
    else:
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)
      print(f'log: account \"{name}\" created')
