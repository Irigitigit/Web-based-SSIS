from flask import Flask
from os import getenv

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    from ssis.api.auth import auth_bp
    from ssis.api.students import students
    from ssis.api.courses import courses
    from ssis.api.colleges import colleges

    app.register_blueprint(auth_bp)
    app.register_blueprint(students)
    app.register_blueprint(courses)
    app.register_blueprint(colleges)

    return app
