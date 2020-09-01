"""
Since we are using divisoinal structure, we’ll define the blueprint in app/admin/views.py.
"""
from flask import Blueprint, render_template
# Creating blueprint for home
admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

# Import the views after home has been defined. The views
# module will need to import 'home' so we need to make
# sure that we import views after home has been defined.

@admin.route("/admin")
@admin.route("/")
def home():

    return render_template("admin/home.html")