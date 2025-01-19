import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from typing import Dict, Optional
from datetime import datetime, timedelta

from configuration.security import JSON_WEB_TOKEN_SECRET_KEY, JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES


class JSONWebToken:
    _secret_key: str
    _algorithm: str

    def __init__(self, *, secret_key: Optional[str] = JSON_WEB_TOKEN_SECRET_KEY, algorithm: Optional[str] = 'HS256'):
        self._secret_key = secret_key

        self._algorithm = algorithm

    def encode(self, payload: Dict, *, expiration_time_minutes: Optional[int] = JSON_WEB_TOKEN_EXPIRATION_TIME_MINUTES):
        payload_ = {
            **payload,
            'exp': datetime.now() + timedelta(minutes=expiration_time_minutes)
        }

        access_token_ = jwt.encode(payload_, self._secret_key, algorithm=self._algorithm)

        return access_token_

    def verify(self, token: str) -> Optional[Dict]:
        try:
            return jwt.decode(token, self._secret_key, algorithms=[self._algorithm])
        except (ExpiredSignatureError, InvalidTokenError) as e:
            print(e)

            return None
