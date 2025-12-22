from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.auth_service import register_user, login_user

# Khởi tạo Blueprint (BẮT BUỘC PHẢI Ở TRÊN)
auth_bp = Blueprint('auth_bp', __name__)

# =====================
# ĐĂNG KÝ
# =====================
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify(message="Missing username or password"), 400

    try:
        register_user(data['username'], data['password'])
        return jsonify(message="User created successfully"), 201
    except ValueError as e:
        return jsonify(message=str(e)), 400


# =====================
# ĐĂNG NHẬP
# =====================
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify(message="Missing username or password"), 400

    token = login_user(data['username'], data['password'])

    if not token:
        return jsonify(message="Invalid credentials"), 401

    return jsonify(access_token=token), 200


# =====================
# ROUTE BẢO VỆ (TEST JWT)
# =====================
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(
        message="Access granted",
        user=current_user
    ), 200
