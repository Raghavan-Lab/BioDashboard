from flask import render_template, flash, redirect, url_for
from app import app
from app.config import TOOLS

# Main Contents Page
@app.route('/')
def contents():
    # Table of Contents is automatically produced from the config.py file
    # To add items, place them into the 'TOOLS' variable as a dict inside the list
    return render_template('content.html', tools=TOOLS)