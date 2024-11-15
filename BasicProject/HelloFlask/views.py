from flask import render_template, request, redirect, url_for, Blueprint 
from HelloFlask.queries import Queries

# Create an instance of the Queries class for database operations
db_queries = Queries()
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template("index.html")

@main_bp.route('/L&F')
def info():
    return render_template('L&F.html')

@main_bp.route('/Items')
def Reportitems():
    return render_template('/items.html')

