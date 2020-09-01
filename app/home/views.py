"""
Since we are using divisoinal structure, we’ll define the blueprint in app/home/__init__.py.
"""
from flask import Blueprint, render_template
# Creating blueprint for home
home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

# Import the views after home has been defined. The views
# module will need to import 'home' so we need to make
# sure that we import views after home has been defined.

@home.route("/")
def get_home():

    return render_template("home/home.html")