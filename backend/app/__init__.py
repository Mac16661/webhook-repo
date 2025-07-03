from flask import Flask
from flask_cors import CORS
from app.webhook.routes import webhook

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(webhook)
    return app