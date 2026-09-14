from fastapi.responses import FileResponse

from jarbinlocalapi.root import jarbinlocalapi, STATIC_DIR


@jarbinlocalapi.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(STATIC_DIR / "images" / "favicon.ico")
