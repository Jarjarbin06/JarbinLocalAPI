from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_root_get():
    url = "http://jarjarbin.local/app"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "App root returned wrong status code")
    Assertion.contain(response.text, "<!DOCTYPE html>", "App root returned wrong response")


# =========================================================
# IMPORT TESTS
# =========================================================


# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_ROOT = JarTest()
failed: list = (
    JTT_APP_ROOT.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_ROOT.run()
