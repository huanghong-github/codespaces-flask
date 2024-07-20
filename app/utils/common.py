from fastapi.responses import JSONResponse


def trueReturn(data, msg, status_code=200):
    """操作成功结果"""
    result = {"status": True, "data": data, "msg": msg}
    return JSONResponse(content=result, status_code=status_code)


def falseReturn(data, msg, status_code=200):
    """操作成功结果"""
    result = {"status": False, "data": data, "msg": msg}
    return JSONResponse(content=result, status_code=status_code)
