from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import uuid

app = Flask("Event Planner")

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    "sqlite:///event_planner.db"
)

db = SQLAlchemy()
db.init_app(app)

from app import models
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.models import User

@login_manager.user_loader
def load_user(id):
    return db.session.get(User, uuid.UUID(id))

from app import routes
