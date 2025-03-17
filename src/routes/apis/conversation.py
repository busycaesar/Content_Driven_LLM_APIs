from flask import Blueprint, request, jsonify
from routes.response import response
from controller.conversation import start_new_conversation, add_prompt, get_conversation

conversation_apis = Blueprint("conversation_apis", __name__)

@conversation_apis.route("/", methods=["POST"])
async def post():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        content_id = data.get("content_id")
        prompt = data.get("prompt") 
        conversation_id = data.get("conversation_id")

        if conversation_id: prompt_response = await add_prompt(conversation_id, prompt)
        else: prompt_response = await start_new_conversation(user_id, content_id, prompt)

        return jsonify(response(True, "Response sent", prompt_response)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@conversation_apis.route("/<conversation_id>", methods=["GET"])
async def get_conversation_id(conversation_id):
    try:
        conversation = await get_conversation(conversation_id)

        return jsonify(response(True, "Conversation sent.", conversation)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500