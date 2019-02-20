from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    Return the index page and details
    '''
    return render_template('index.html')
