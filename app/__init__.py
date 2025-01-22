"""
Module for initializing the Flask application.

Creates an instance of the Flask application and configures it.
"""

from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Import routes after creating the app to avoid circular imports
from app import routes