from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_cpu_get():
    url = "http://jarjarbin.local/app/system/cpu"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)

    Assertion.eq(response.status_code, 200, "APP system cpu returned wrong status code")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_CPU = JarTest()
failed: list = (
    JTT_APP_SYSTEM_CPU.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_CPU.run()
