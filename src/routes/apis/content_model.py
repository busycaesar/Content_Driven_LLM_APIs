from flask import Blueprint, request, jsonify
from routes.response import response
from controllers import ContentModelController

content_model_apis = Blueprint("content_model_apis", __name__)

@content_model_apis.route("/<collection_id>", methods=["PUT"])
async def put_content_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        model_id = data.get("model_id")

        content_model_controller = ContentModelController(user_id, collection_id)

        await content_model_controller.update(model_id)

        return jsonify(response(True, "Content Model updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_model_apis.route("/<collection_id>", methods=["GET"])
async def get_content_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        content_model_controller = ContentModelController(user_id, collection_id)

        content_model = await content_model_controller.get()

        return jsonify(response(True, "Content Model sent.", content_model)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500