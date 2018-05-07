# encoding: utf-8
#__author__ = 'poet'
# 4/28/18

from flask import Flask
from flask_migrate import Migrate

from simpledu.config import configs
from .models import db





def register_blueprints(app):
    from .handlers import  front,course,admin
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)



def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    Migrate(app,db)
    return app
