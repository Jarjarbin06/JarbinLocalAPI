from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_root_get():
    url = "http://jarjarbin.local/api"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "API root returned wrong status code")
    Assertion.eq({"message": "Hello World!"}, response.json(), "API root returned wrong response")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_API.JT_System import JT_api_system_root


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_ROOT = JarTest()
failed: list = (
    JTT_API_ROOT.fetch()
    + JT_api_system_root.failed
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_ROOT.run()
