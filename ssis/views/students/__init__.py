from flask import Blueprint

student = Blueprint("student", __name__, url_prefix="/students-ui")

from . import routes