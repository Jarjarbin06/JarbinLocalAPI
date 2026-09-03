from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_root_get():
    url = "http://jarjarbin.local/"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request.show(response.request.method, url)
    Show.Response.show(response)

    Assertion.eq(
        response.status_code,
        200
    )


# =========================================================
# REGISTER TEST
# =========================================================

JTT_ROOT = JarTest()
failed: list = JTT_ROOT.fetch()
