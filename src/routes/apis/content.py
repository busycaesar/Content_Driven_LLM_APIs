from flask import Blueprint, request, jsonify
from routes.response import response

content_apis = Blueprint("content_apis", __name__)

@content_apis.route("/", methods=["POST"])
async def post():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/", methods=["GET"])
async def get():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@content_apis.route("/:contentId", methods=["GET"])
async def get_content_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/:contentId", methods=["PUT"])
async def put_content_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
    
@content_apis.route("/:contentId", methods=["DELETE"])
async def delete_content_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500
