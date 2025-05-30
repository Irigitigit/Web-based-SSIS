from flask import Flask
from os import getenv
from flask_jwt_extended import JWTManager  # ✅ import JWT
from ssis.api import api

def create_app() -> object:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY') or 'super-secret-key'

    # ✅ Required config for Flask-JWT-Extended
    app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY') or 'jwt-secret-key'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    # ✅ Initialize JWT
    jwt = JWTManager(app)

    # import blueprints
    from .views.admin import admin
    from .views.students import student
    from .views.courses import course
    from .views.colleges import college

    # register blueprints
    app.register_blueprint(api)
    app.register_blueprint(admin)
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    return app
