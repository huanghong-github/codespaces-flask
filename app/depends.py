from typing import Annotated, Optional

from fastapi import Depends, Header
from sqlalchemy.orm.session import Session

from app.core.database import get_db
from app.models.user import User
from app.services.user_service import UserService
from app.utils import common
from app.utils.token import Token

SessionDep = Annotated[Session, Depends(get_db)]


def get_current_user_id(token=Header()):
    try:
        payload = Token.decode_access_token(token)
        return payload["data"]["user_id"]
    except:
        return None


CurrentUserDep = Annotated[Optional[int], Depends(get_current_user_id)]


def authorize(session: SessionDep, token=Header()):
    """
    用户鉴权
    :return: list
    """
    try:
        payload = Token.decode_access_token(token)
        user_id = payload["data"]["user_id"]
        login_time = payload["data"]["login_time"]

        user = UserService(session).get_user_by_id(user_id)
        if user is None:
            return common.falseContent("", "找不到该用户信息")
        else:
            if user.login_time != login_time:
                return common.falseContent("", "Token已更改,请重新登录获取")
    except:
        return common.falseContent("", "Token已过期,请重新登录获取")
    return token


AuthsDep = Depends(authorize)
