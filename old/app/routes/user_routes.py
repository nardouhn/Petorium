from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user_model import User
from app.extensions import db


user_bp = Blueprint('user_bp', __name__)

# 🧩 Lấy danh sách tất cả user (chỉ admin hoặc user đã đăng nhập)
@user_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    result = [{"id": u.id, "username": u.username} for u in users]
    return jsonify(result), 200


# 🔍 Lấy thông tin 1 user theo id
@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({"id": user.id, "username": user.username}), 200


# ✏️ Cập nhật thông tin user (chỉ user đó mới được sửa)
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404
    if user.username != current_user:
        return jsonify({"message": "Permission denied"}), 403

    data = request.get_json()
    if "password" in data:
        user.hash_password(data["password"])
    db.session.commit()
    return jsonify({"message": "User updated successfully"}), 200


# ❌ Xóa user (chỉ chính họ mới được xóa)
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404
    if user.username != current_user:
        return jsonify({"message": "Permission denied"}), 403

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200

