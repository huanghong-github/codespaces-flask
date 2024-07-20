import random
import re
import string
import time
import traceback

from fastapi import APIRouter
from fastapi.logger import logger

from app.depends import SessionDep
from app.models.user import User, UserBase, UserRegist
from app.services.user_service import UserService
from app.utils import common
from app.utils.email import Email
from app.utils.passwordutil import PasswordUtil
from app.utils.token import Token

router = APIRouter()


@router.post("/login")
async def login(user_login: UserBase, session: SessionDep):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    us = UserService(session)
    user = us.get_user_by_email(user_login.email)
    if not user or not PasswordUtil.verify_password(user_login.password, user.password):
        session.close()
        return common.falseReturn({}, "login failed")

    try:
        login_time = int(time.time())
        origin_data = {"user_id": user.id, "login_time": login_time}
        token = Token.create_access_token(origin_data=origin_data)
        user.login_time = login_time
        us.save(user)
        return common.trueReturn(
            {
                "token": token,
                "user_id": user.id,
                "user_name": user.user_name,
                "email": user.email,
            },
            "login successfully",
        )
    except:
        logger.error(f"login error: {traceback.format_exc()}")
        return common.falseReturn({}, "login failed")


@router.post("/regist")
async def regist(user_regist: UserRegist, session: SessionDep):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    us = UserService(session)
    if us.get_user_by_email(user_regist.email):
        return common.falseReturn({}, "user already exists")

    if user_regist.verify_code != "123456":
        return common.falseReturn({}, "verify_code incorrect")
    password = user_regist.password
    if PasswordUtil.password_check(password):
        user = User(
            email=user_regist.email,
            user_name=user_regist.user_name,
            password=PasswordUtil.password_hash(password),
        )
        us.save(user)
        return common.falseReturn({}, "regist successfully")
    else:
        return common.falseReturn({}, "password is too simple")


@router.post("/send_email")
async def send_email(request, session: SessionDep):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    email = request.POST.get("email")
    us = UserService(session)
    if us.get_user_by_email(email):
        verify_code = "".join(random.sample(string.digits + string.ascii_lowercase, 6))
        Email.send(
            email_to=email,
            subject="注册验证码",
            html_content=f"您的验证码是：{verify_code}",
        )
        return common.trueReturn({}, "send successfully")
    else:
        return common.falseReturn({}, "this email has been registed")
