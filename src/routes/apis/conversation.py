from flask import Blueprint, request, jsonify
from routes.response import response
from controllers import ConversationController

conversation_apis = Blueprint("conversation_apis", __name__)

@conversation_apis.route("/", methods=["POST"])
async def post():
    try:
        data = request.get_json()
        api_key = data.get("api_key")
        collection_id = data.get("collection_id")
        prompt = data.get("prompt")
        conversation_id = data.get("conversation_id")

        conversation_controller = ConversationController(
            api_key,
            collection_id,
            conversation_id
        )

        prompt_response, conversation_id = await conversation_controller.add(prompt)

        return jsonify(response(True, "Response sent", {
            "response": prompt_response,
            "conversation_id": conversation_id
        })), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500

@conversation_apis.route("/<conversation_id>", methods=["GET"])
async def get_conversation_id(conversation_id):
    try:
        conversation_controller = ConversationController(conversation_id)

        conversation = await conversation_controller.get()

        return jsonify(response(True, "Conversation sent.", conversation)), 201
    except Exception as e:
        return jsonify(response(False, f"Error: {str(e)}")), 500