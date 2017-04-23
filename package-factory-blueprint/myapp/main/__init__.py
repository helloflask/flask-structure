from flask import Blueprint

main = Blueprint('main', __name__)

from myapp.main import views