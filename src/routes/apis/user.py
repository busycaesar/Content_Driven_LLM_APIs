from flask import Blueprint, request, jsonify
from routes.response import response
from controllers.user import register_user, validate_user, update_password, get_user, delete_user

user_apis = Blueprint("user_apis", __name__)

@user_apis.route("/register", methods=["POST"])
async def post_register():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        jwt = await register_user(name, email, password)

        return jsonify(response(True, "New user registered.", jwt)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@user_apis.route("/validate", methods=["POST"])
async def post_validate():
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        jwt = await validate_user(email, password)

        return jsonify(response(True, "User successfully varified", jwt)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@user_apis.route("/password", methods=["PATCH"])
async def patch_password():
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()

        old_password = data.get("old_password")
        new_password = data.get("new_password")

        await update_password(user_id, old_password, new_password)

        return jsonify(response(True, "The user's password is updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@user_apis.route("/", methods=["GET"])
async def get():
    try:
        # Get user id from jwt token.
        user_id = 1

        user_info = await get_user(user_id)

        return jsonify(response(True, "User information sent.", user_info)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@user_apis.route("/", methods=["DELETE"])
async def delete():
    try:
        # Get user id from jwt token.
        user_id = 1

        await delete_user(user_id)

        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
