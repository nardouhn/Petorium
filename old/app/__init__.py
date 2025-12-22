from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import SECRET_KEY
from app.extensions import db, bcrypt
from app.routes.auth_routes import auth_bp
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['JWT_SECRET_KEY'] = SECRET_KEY

    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")

    return app
