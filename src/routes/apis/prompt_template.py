from flask import Blueprint, request, jsonify
from routes.response import response
from controllers import PromptTemplateController

prompt_template_apis = Blueprint("prompt_template_apis", __name__)

@prompt_template_apis.route("/<collection_id>", methods=["PUT"])
async def put_collection_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1
        data = request.get_json()
        prompt_template = data.get("prompt_template")

        prompt_template_controller = PromptTemplateController(
            user_id,
            collection_id)

        await prompt_template_controller.update(prompt_template)

        return jsonify(response(True, "Prompt template updated.")), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@prompt_template_apis.route("/<collection_id>", methods=["GET"])
async def get_collection_id(collection_id):
    try:
        # Get user id from jwt token.
        user_id = 1

        prompt_template_controller = PromptTemplateController(
            user_id,
            collection_id)

        prompt_template = await prompt_template_controller.get()

        return jsonify(response(True, "Prompt template sent.", prompt_template)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500