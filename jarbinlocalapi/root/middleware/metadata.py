from json import loads
from fastapi import Request
from fastapi.responses import JSONResponse

from jarbin_toolkit_time import StopWatch

from jarbinlocalapi import (
    __name__ as name,
    __version__ as version
)
from jarbinlocalapi.root import jarbinlocalapi


@jarbinlocalapi.middleware("http")
async def api_metadata_middleware(request: Request, call_next):

    if request.url.path.startswith("/app") or request.url.path == "/openapi.json":
        return await call_next(request)

    meta = request.query_params.get("meta", "true").lower() == "true"

    sw = StopWatch(start=True)

    response = await call_next(request)

    elapsed = sw.elapsed()

    if not meta or not response.headers.get("content-type", "").startswith("application/json"):
        return response

    body = b""

    async for chunk in response.body_iterator:
        body += chunk

    return JSONResponse(
        status_code=response.status_code,
        content={
            "data": loads(body),
            "meta": {
                "api": name,
                "version": version,
                "response_time_s": round(elapsed, 3),
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
            },
        },
    )
