from app.models.user_model import User
from app.extensions import db
from flask_jwt_extended import create_access_token


def register_user(username, password):
    """
    Đăng ký user mới
    """
    if User.query.filter_by(username=username).first():
        raise ValueError("User already exists")

    user = User(username=username)
    user.hash_password(password)

    db.session.add(user)
    db.session.commit()

    return user


def login_user(username, password):
    """
    Đăng nhập và trả về JWT access token
    """
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return None

    access_token = create_access_token(
        identity=str(user.id),          # 🔑 BẮT BUỘC STRING
        additional_claims={
            "username": user.username,
            "role": user.role
        }
    )

    return access_token
