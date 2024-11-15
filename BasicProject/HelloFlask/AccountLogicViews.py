from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from HelloFlask.queries import Queries  # Assuming Queries class handles database operations for accounts
from werkzeug.security import generate_password_hash, check_password_hash

# Instance of Queries for database access
db_queries = Queries()
account_bp = Blueprint('account', __name__)

@account_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create account in the database
        db_queries.createAccount(username, hashed_password, email)
        
        return redirect(url_for('account.login'))
    
    return render_template('AccountLogic/signup.html')

@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['NetId']
        password = request.form['password']
        email = request.form['email']
        # Retrieve user information from the database
        user = db_queries.getUser(username, email)  # Assume `get_user` retrieves user data

        # Validate user and password
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            return redirect(url_for('main.home'))
        else:
            flash("Invalid username or password.")

    # Render the login page if GET request or failed login
    return render_template('AccountLogic/login.html')

