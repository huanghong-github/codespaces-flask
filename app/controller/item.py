from fastapi import APIRouter

from app.depends import AuthsDep, CurrentUserDep
from app.utils import common

router = APIRouter()


@router.post("/list", dependencies=[AuthsDep])
async def item_list(user_id: CurrentUserDep):
    print(user_id)
    return common.trueReturn({"items": ["hello", "world"]}, "登录成功")
