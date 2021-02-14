from flask import Flask
from flask_migrate import Migrate
from os import path, environ
from flask_login import LoginManager
from . import db


def create_app():
  '''
  Creates flask app to serve it
  '''
  # the values of Postgresql
  POSTGRES_PATH = "database.db"
  POSTGRES_URL = "localhost:5432"
  POSTGRES_USER = "postgres"
  POSTGRES_PW = "postgres"
  POSTGRES_DB = "postgres"
  
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lolxd123'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  
  from src.views import views
  from src.auth import auth
  from src.profile import profile
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(profile, url_prefix='/')
  
  from src.models import User
  
  if not path.exists('/'+POSTGRES_PATH):
    db.create_all(app=app)
    print('success: created database')
  
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)
  
  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  return app