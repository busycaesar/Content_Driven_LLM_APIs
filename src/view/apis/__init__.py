from flask import Blueprint
from view.apis.content import content_apis
from view.apis.prompt import prompt_apis

apis = Blueprint("apis", __name__)

apis.register_blueprint(content_apis, url_prefix="/content")
apis.register_blueprint(prompt_apis, url_prefix="/prompt")