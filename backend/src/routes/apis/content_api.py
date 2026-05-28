from flask import Blueprint, request, jsonify, g
from routes.response import response
from routes.middleware import require_auth
from controllers import ContentController

content_apis = Blueprint("content_apis", __name__)

@content_apis.route("/", methods=["POST"])
@require_auth
async def post():
    try:
        user_id = g.user_id
        data = request.get_json()
        content = data.get("content")

        content_controller = ContentController(user_id)

        collection_id = await content_controller.add(content)

        return jsonify(response(True, "New content is stored.", collection_id)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/", methods=["GET"])
@require_auth
async def get():
    try:
        user_id = g.user_id

        content_controller = ContentController(user_id)

        content = await content_controller.get_all()

        return jsonify(response(True, "All the content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/<collection_id>", methods=["GET"])
@require_auth
async def get_collection_id(collection_id):
    try:
        user_id = g.user_id

        content_controller = ContentController(user_id, collection_id)

        content = await content_controller.get()

        return jsonify(response(True, "Content sent.", content)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<collection_id>", methods=["PUT"])
@require_auth
async def put_collection_id(collection_id):
    try:
        user_id = g.user_id
        data = request.get_json()
        content = data.get("content")
        
        content_controller = ContentController(user_id, collection_id)

        await content_controller.update(content)

        return jsonify(response(True, "Content Updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/<collection_id>", methods=["DELETE"])
@require_auth
async def delete_collection_id(collection_id):
    try:
        user_id = g.user_id

        content_controller = ContentController(user_id, collection_id)

        await content_controller.delete()

        return jsonify(response(True, "Delete stored content.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500