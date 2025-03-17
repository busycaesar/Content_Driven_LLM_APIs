from flask import Blueprint, request, jsonify
from routes.response import response
from controller.prompt_template import update_prompt_template, get_prompt_template

prompt_template_apis = Blueprint("prompt_template_apis", __name__)

@prompt_template_apis.route("/<content_id>", methods=["PUT"])
async def put_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        prompt_template = data.get("prompt_template")

        await update_prompt_template(user_id, content_id, prompt_template)

        return jsonify(response(True, "Prompt template updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@prompt_template_apis.route("/<content_id>", methods=["GET"])
async def get_content_id(content_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        prompt_template = await get_prompt_template(user_id, content_id)

        return jsonify(response(True, "Prompt template sent.", prompt_template)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500