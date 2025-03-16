from flask import Blueprint, request, jsonify
from routes.response import response

user_apis = Blueprint("user_apis", __name__)

@user_apis.route("/register", methods=["POST"])
async def post_register():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@user_apis.route("/validate", methods=["POST"])
async def post_validate():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@user_apis.route("/password", methods=["PATCH"])
async def patch_password():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@user_apis.route("/", methods=["GET"])
async def get():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@user_apis.route("/", methods=["DELETE"])
async def delete():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
