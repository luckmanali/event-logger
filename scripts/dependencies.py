from fastapi import Header, HTTPException
from jwt_utils import decode_jwt_token
import os

app_secret = os.getenv("APP_SECRET")


async def authenticate_app(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    token = authorization.split("Bearer ")[-1]
    app_data = decode_jwt_token(token, os.getenv("APP_SECRET"))

    if app_data.get("app_name") != "your_flutter_app":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return app_data
