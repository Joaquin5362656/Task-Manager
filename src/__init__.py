from flask import Flask
from src.config import Config
from src.extensions import mongo, jwt
from src.auth.routes import auth_bp
from src.tasks.routes import tasks_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/api')

    return app