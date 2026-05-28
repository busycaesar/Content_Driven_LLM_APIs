import functools
import jwt as pyjwt
from flask import request, jsonify, g
from routes.response import response
from utils import EnvVars

def require_auth(f):
    @functools.wraps(f)
    async def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")

        if not auth_header.startswith("Bearer "):
            return jsonify(response(False, "Unauthorized.")), 401

        token = auth_header[len("Bearer "):]

        try:
            payload = pyjwt.decode(token, EnvVars.JWT_SECRET, algorithms=["HS256"])
            g.user_id = payload["user_id"]
        except Exception:
            return jsonify(response(False, "Unauthorized.")), 401

        return await f(*args, **kwargs)

    return decorated
