from flask import Blueprint, Response, request, json
from flask_cors import cross_origin
from src.models import User
from werkzeug.security import check_password_hash, generate_password_hash

from .. import db
from src.auth.utils import generate_token

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
@cross_origin()
def login():
  '''
  Login user
  '''
  data = request.get_json()
  name = data["name"]
  password = data["password"]
  
  if name == None:
    print(f'log: no form request, login')
    return Response(status=409) # already exists
  
  user = User.query.filter_by(name=name).first()
  token = user.token
  
  if user:
    if check_password_hash(user.password, password):
      print(f'log: account \"{name}\" logged')
      return json.dumps({"token":token}), 202
      #return Response(status=202) # success
    else:
      print(f'log: login \"{name}\" failed -> bad password')
      return Response(status=401) # bad password
  else:
    print(f'log: account \"{name}\" does\'t exist')
    return Response(status=404) # bad username, doesn't exists


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
  '''
  Create new object user and login to the service, sign up user
  '''
  data = request.get_json()
  name = data["name"]
  password = data["password"]
  
  if name == None:
    print(f'log: no form request, signup')
    return Response(status=409) # already exists
  
  ip = request.remote_addr
  gen_passwd = generate_password_hash(password, method='sha256')
  gen_token = generate_token()
  
  # if token exists generate new again
  while(bool(User.query.filter_by(token=gen_token).first())):
    gen_token = generate_token()
    
  new_user = User(
    name = name,
    token = gen_token,
    password = gen_passwd,
    ip = ip
  )
    
  if bool(User.query.filter_by(name=name).first()):
    print(f'log: account \"{name}\" didn\'t created -> exists')
    return Response(status=409) # already exists
  else:
    db.session.add(new_user)
    db.session.commit()
    print(f'log: account \"{name}\" created')
    return Response(status=201) # success
