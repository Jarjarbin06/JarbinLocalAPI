from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_root_get():
    url = "http://jarjarbin.local/app/"

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

JTT_APP_ROOT = JarTest()
failed: list = JTT_APP_ROOT.fetch()
