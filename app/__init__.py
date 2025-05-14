from flask import Flask

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Use the config class passed as parameter

    from .routes import main
    app.register_blueprint(main)

    return app
