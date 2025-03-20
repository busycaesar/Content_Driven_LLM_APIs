from flask import Blueprint, request, jsonify
from routes.response import response
from controllers.llm import get_available_llms

llm_apis = Blueprint("llm_apis", __name__)

@llm_apis.route("/", methods=["GET"])
async def get():
    try:
        available_llms = await get_available_llms()

        return jsonify(response(True, "Available LLMs sent.", available_llms)), 200
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500