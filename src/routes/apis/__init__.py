from flask import Blueprint
from routes.apis.user import user_apis
from routes.apis.content import content_apis
from routes.apis.prompt_template import prompt_template_apis
from routes.apis.llm import llm_apis
from routes.apis.content_model import content_model_apis
from routes.apis.conversation import conversation_apis

apis = Blueprint("apis", __name__)

apis.register_blueprint(user_apis, url_prefix="/user")
apis.register_blueprint(content_apis, url_prefix="/content")
apis.register_blueprint(prompt_template_apis, url_prefix="/prompt_template")
apis.register_blueprint(llm_apis, url_prefix="/llm")
apis.register_blueprint(content_model_apis, url_prefix="/content_model")
apis.register_blueprint(conversation_apis, url_prefix="/conversation")
