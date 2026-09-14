from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show, Context


# =========================================================
# TESTS
# =========================================================

def JT_fastapi_get_docs():
    url = "http://jarjarbin.local/docs"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "FastAPI docs returned wrong status code")


def JT_fastapi_get_redoc():
    url = "http://jarjarbin.local/redoc"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "FastAPI redoc returned wrong status code")


def JT_fastapi_get_openapi():
    url = "http://jarjarbin.local/openapi.json"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "FastAPI openapi.json returned wrong status code")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_FASTAPI = JarTest()
failed: list = (
    JTT_FASTAPI.fetch()
)

if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_FASTAPI.run()
