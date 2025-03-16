from flask import Blueprint, request, jsonify
from routes.response import response

llm_apis = Blueprint("llm_apis", __name__)

@llm_apis.route("/", methods=["GET"])
async def get():
    try:
        return jsonify(response(True, "New content stored.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500