from flask import request, current_app
import jwt

def get_current_user():
    token = request.headers.get("Authorization")

    if not token:
        return None

    try:
        decoded = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=["HS256"]
        )
        return decoded["user_id"]
    except:
        return None