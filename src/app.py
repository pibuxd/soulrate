from os import environ, path

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from . import db


def create_app():
  '''
  Creates flask app to serve it
  :return app: database and flask
  '''
  # the values of Postgresql
  DB_PATH = "database.db"
  POSTGRES_URL = "localhost:5432"
  POSTGRES_USER = "postgres"
  POSTGRES_PW = "postgres"
  POSTGRES_DB = "postgres"
  
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lolxd123'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
  #app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  
  from src.auth import auth
  from src.profile import profile
  from src.views import views
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(profile, url_prefix='/')
  
  from src.models import User
  
  create_database(app, DB_PATH)
  
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)
  
  @login_manager.user_loader
  def load_user(id:int):
    return User.query.get(int(id))
  
  return app

def create_database(app, DB_PATH:str):
  '''
  Create new database
  :param DB_PATH: database's path
  :param app: database
  '''
  if not path.exists('src/' + DB_PATH):
      db.create_all(app=app)
      print('success: database created')
