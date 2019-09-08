from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_restful import Api

from src.routes import add_routes
from database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mobile_recharge.db'
    api = Api(app)
    add_routes(api)

    from src.models.company import Company
    from src.models.product import Product
    from src.models.recharge import Recharge
    db.app = app
    db.init_app(app)
    Migrate(app, db)

    return app
