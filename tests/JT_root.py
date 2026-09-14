from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show, Context


# =========================================================
# TESTS
# =========================================================

def JT_root_get():
    url = "http://jarjarbin.local/"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Root returned wrong status code")
    Assertion.eq({"status": "OK"}, response.json()["data"], "Root returned wrong response")


def JT_root_get_metadata():
    url = "http://jarjarbin.local/"

    response = Get.HTTP.get(
        url,
        follow_redirects=True
    )

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Root returned wrong status code")
    Assertion.contain(response.json()["meta"], "path", "Root returned wrong response")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_API import JT_api_root
from tests.JT_APP import JT_app_root


# =========================================================
# REGISTER TEST
# =========================================================

JTT_ROOT = JarTest(
    context=Context(
        command=[
            ("make --no-print-directory start", "make --no-print-directory stop")
        ]
    )
)
failed: list = (
    JTT_ROOT.fetch()
    + JT_api_root.failed
    + JT_app_root.failed
)

if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_ROOT.run()
