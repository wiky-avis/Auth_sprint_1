from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from src.api.technical.ping import api as ping_api
from src.api.v1.auth.checking_mail import api as check_mail

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


cors = CORS()
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def init_db(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)

    return db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    init_db(app)

    api = Api(
        app=app,
        title="API Auth",
        description="API для авторизации пользователей",
        doc="/api/swagger/",
        version="1.0.0",
    )
    api.add_namespace(ping_api)
    api.add_namespace(check_mail)

    cors.init_app(app)

    return app
