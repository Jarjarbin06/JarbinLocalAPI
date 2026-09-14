from jarbinlocalapi.root import jarbinlocalapi


@jarbinlocalapi.get("/")
def get_root():
    """
    Route: `/`

    Get server status.
    """
    return {"status": "OK"}
