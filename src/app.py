from os import environ, path

from flask import Flask
from flask_cors import CORS
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
  
  cors = CORS(app, resources={r"/*": {"origins": "*"}}) # !IMPORTANT
  app.config["CORS_SUPPORTS_CREDENTIALS"] = True    # !IMPORTANT
  app.config['CORS_ALLOW_HEADERS'] = 'Content-Type' # !IMPORTANT
  
  app.config['SECRET_KEY'] = 'lolxd123'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
  #app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  db.init_app(app)
  
  from src.api.auth import auth
  from src.api.home import views
  from src.api.profile import profile
  from src.api.rating import rating
  
  app.register_blueprint(views, url_prefix='/api')
  app.register_blueprint(auth, url_prefix='/api')
  app.register_blueprint(profile, url_prefix='/api')
  app.register_blueprint(rating, url_prefix='/api')
  
  from src.models import User
  
  create_database(app, DB_PATH)
  
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
