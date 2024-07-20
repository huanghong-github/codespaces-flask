import time

import jwt

from app.core.settings import settings


class Token:

    @staticmethod
    def create_access_token(origin_data):
        """
        生成认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                "exp": (int(time.time()) + settings.ACCESS_TOKEN_EXPIRE_SECONDS),
                "iat": int(time.time()),
                "iss": "paperpie",
                "data": origin_data,
            }

            encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)

            bearer_token = "Bearer " + encoded_jwt
            return bearer_token
        except Exception as e:
            return e

    @staticmethod
    def decode_access_token(bearer_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """

        try:
            auth_tokenArr = bearer_token.split(" ")
            if (
                auth_tokenArr
                and auth_tokenArr[0] == "Bearer"
                and len(auth_tokenArr) == 2
            ):
                secret_key = settings.SECRET_KEY
                algorithm = settings.ALGORITHM

                payload = jwt.decode(
                    auth_tokenArr[1],
                    secret_key,
                    algorithms=[algorithm],
                    options={"verify_exp": True},
                )
                return payload
        except jwt.ExpiredSignatureError:
            return "Token过期"
        except jwt.InvalidTokenError:
            return "无效Token"
