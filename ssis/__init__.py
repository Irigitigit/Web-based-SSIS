from flask import Flask
from os import getenv
from flask_jwt_extended import JWTManager  # You'll also need this
from dotenv import load_dotenv
from flask import Flask
from flasgger import Swagger

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = getenv('SECRET_KEY')

    Swagger(app)

    # Register your Blueprints/routes here
    from ssis.api.auth import auth as auth_bp
    from ssis.api.students import students as students_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)

    return app

def create_app() -> object:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = getenv('SECRET_KEY')  # for JWT

    # Initialize JWT
    jwt = JWTManager(app)

    # import blueprints
    from .views.admin import admin
    from .views.students import student
    from .views.courses import course
    from .views.colleges import college

    from .api.auth import auth
    from .api.students import students
    from .api.colleges import colleges
    from .api.courses import courses

    # register blueprints
    app.register_blueprint(admin)
    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)

    app.register_blueprint(auth)
    app.register_blueprint(students)
    app.register_blueprint(colleges)
    app.register_blueprint(courses)

    return app
