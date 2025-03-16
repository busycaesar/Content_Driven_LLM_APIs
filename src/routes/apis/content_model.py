from flask import Blueprint, request, jsonify
from routes.response import response

content_model_apis = Blueprint("content_model_apis", __name__)

@content_model_apis.route("/:contentId", methods=["PUT"])
async def put_content_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_model_apis.route("/:contentId", methods=["GET"])
async def get_content_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500