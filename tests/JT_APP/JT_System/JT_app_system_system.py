from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_system_get():
    url = "http://jarjarbin.local/app/system/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "APP system system returned wrong status code")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_SYSTEM = JarTest()
failed: list = (
    JTT_APP_SYSTEM_SYSTEM.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_SYSTEM.run()
