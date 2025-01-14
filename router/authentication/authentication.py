from router.router import authentication_router


@authentication_router.get("/login")
async def login():
    return {
        "location": "/login"
    }
