from flask import Blueprint, request, jsonify
from routes.response import response
from controllers import ContentController

content_apis = Blueprint("content_apis", __name__)

@content_apis.route("/", methods=["POST"])
async def post():
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        content = data.get("content")

        content_controller = ContentController(user_id)

        collection_id = await content_controller.add(content)

        return jsonify(response(True, "New content is stored.", collection_id)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/", methods=["GET"])
async def get():
    try:
        # Get user id from jwt token.
        user_id = 1

        content_controller = ContentController(user_id)

        content = await content_controller.get_all()

        return jsonify(response(True, "All the content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/<collection_id>", methods=["GET"])
async def get_collection_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        content_controller = ContentController(user_id, collection_id)

        content = await content_controller.get()

        return jsonify(response(True, "Content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<collection_id>", methods=["PUT"])
async def put_collection_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        content = data.get("content")
        
        content_controller = ContentController(user_id, collection_id)

        await content_controller.update(content)

        return jsonify(response(True, "Content Updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<collection_id>", methods=["DELETE"])
async def delete_collection_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        content_controller = ContentController(user_id, collection_id)

        await content_controller.delete()

        return jsonify(response(True, "Delete stored content.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500