from flask import Blueprint, request, jsonify
from routes.response import response
from controller.content import store_new_content, get_all_content, get_stored_content, update_stored_content, delete_stored_content

content_apis = Blueprint("content_apis", __name__)

@content_apis.route("/", methods=["POST"])
async def post():
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        content = data.get("content")

        collection_id = await store_new_content(user_id, content)

        return jsonify(response(True, "New content is stored.", collection_id)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/", methods=["GET"])
async def get():
    try:
        # Get user id from jwt token.
        user_id = 1
        content = await get_all_content(user_id)

        return jsonify(response(True, "All the content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/<content_id>", methods=["GET"])
async def get_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        content = await get_stored_content(user_id, content_id)

        return jsonify(response(True, "Content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<content_id>", methods=["PUT"])
async def put_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        content = data.get("content")
        
        await update_stored_content(user_id, content_id, content)

        return jsonify(response(True, "Content Updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<content_id>", methods=["DELETE"])
async def delete_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        await delete_stored_content(user_id, content_id)

        return jsonify(response(True, "Delete stored content.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500