import jwt
import datetime
from fastapi import HTTPException


def create_jwt_token(data: dict, secret: str, expiration: datetime.timedelta):
    payload = {
        "exp": datetime.datetime.utcnow() + expiration,
        "data": data,
    }
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token


def decode_jwt_token(token: str, secret: str, algorithms=["HS256"]):
    try:
        payload = jwt.decode(token, secret, algorithms=algorithms)
        return payload["data"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
