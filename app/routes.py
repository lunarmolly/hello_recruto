"""
Module for defining routes in the Flask application.

Contains request handlers for various URLs.
"""

from flask import request
from app import app

@app.route('/')
def hello():
    """
    Handler for the root URL (/).

    Returns a message with values substituted from the GET request.
    If parameters are not provided, default values are used.

    :returns: A message in the format "Hello {name}! {message}!".
    :rtype: str
    """
    name = request.args.get('name', 'Recruto')  # Get the value of the 'name' parameter from the request
    message = request.args.get('message', 'Let\'s be friends')  # Get the value of the 'message' parameter from the request
    return f'Hello {name}! {message}!'