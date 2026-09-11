from jarbinlocalapi.api import api


#-------------------- ROOT --------------------#

@api.get("/")
async def get_api():
    """
        Route: `/api`

        Return base "Hello World!" message.
    """

    return {"message": "Hello World!"}
