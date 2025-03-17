from flask import Blueprint, request, jsonify
from routes.response import response
from controller.content_model import update_content_model, get_content_model

content_model_apis = Blueprint("content_model_apis", __name__)

@content_model_apis.route("/<content_id>", methods=["PUT"])
async def put_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        model_id = data.get("model_id")

        await update_content_model(user_id, content_id, model_id)

        return jsonify(response(True, "Content Model updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_model_apis.route("/<content_id>", methods=["GET"])
async def get_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        content_model = await get_content_model(user_id, content_id)

        return jsonify(response(True, "Content Model sent.", content_model)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500