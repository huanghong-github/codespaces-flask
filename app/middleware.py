import time
from starlette.middleware.base import BaseHTTPMiddleware


async def process_time(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


def regist_middleware(app):
    app.add_middleware(BaseHTTPMiddleware, dispatch=process_time)
    pass
