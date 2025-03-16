from flask import Blueprint, request, jsonify
from routes.response import response

conversation_apis = Blueprint("conversation_apis", __name__)

@conversation_apis.route("/", methods=["POST"])
async def post():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@conversation_apis.route("/:conversationId", methods=["GET"])
async def get_conversation_id():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500