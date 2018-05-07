# encoding: utf-8
#__author__ = 'poet'
# 4/28/18

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from simpledu.config import configs
from .models import db, User


def register_blueprints(app):
    from .handlers import  front,course,admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

def register_extesions(app):
    db.init_app(app)
    Migrate(app,db)

    login_manage = LoginManager()
    login_manage.init_app(app)

    @login_manage.user_loader
    def user_loader(id):
        return  User.query.get(id)

    login_manage.login_view = 'front.login'

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_blueprints(app)
    register_extesions(app)
    return app
