from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

class JWTManager:
    def __init__(self, secret_key, algorithm="HS256", access_token_expire_minutes=30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        access_token_expires = timedelta(minutes=self.access_token_expire_minutes)
        expire = datetime.now(timezone.utc) + access_token_expires
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except InvalidTokenError:
            return None
