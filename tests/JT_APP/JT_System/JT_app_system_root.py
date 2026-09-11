from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_root_get():
    url = "http://jarjarbin.local/app/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "APP system root returned wrong status code")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_APP.JT_System import JT_app_system_cpu
from tests.JT_APP.JT_System import JT_app_system_memory



# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_ROOT = JarTest()
failed: list = (
        JTT_APP_SYSTEM_ROOT.fetch()
        + JT_app_system_cpu.failed
        + JT_app_system_memory.failed
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_ROOT.run()
