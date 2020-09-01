from flask import Flask, render_template
from app.home.views import home
from app.admin.views import admin


def create_app():
    app = Flask(__name__)
    
    # check the ENV variable, and load the specifig configuration
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    
    # Get the environment
    print(f"Flask App Environment is set to: {app.config['ENV']}")

    #Register Blueprints
    app.register_blueprint(home, url_prefix="/home") 
    app.register_blueprint(admin, url_prefix="/admin") 


    return app

