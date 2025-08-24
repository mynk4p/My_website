import sqlite3
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# This line is the main change for security
app.secret_key = os.environ.get('SECRET_KEY', 'a-default-key-for-local-development')
DATABASE = '/home/mynk4p/mysite/portfolio.db'

# --- Database Helper Functions ---
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db