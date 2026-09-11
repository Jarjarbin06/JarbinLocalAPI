from jarbinlocalapi.updater import updater


#-------------------- ROOT --------------------#

@updater.get("/")
async def get_updater():
    """
        Route: `/updater`

        Return base "Hello World!" message.
    """

    return {"message": "Hello World!"}
