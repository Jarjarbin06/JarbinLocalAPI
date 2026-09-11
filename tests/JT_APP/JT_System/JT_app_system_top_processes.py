from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_top_processes_get():
    url = "http://jarjarbin.local/app/system/top_processes"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "APP system top_processes returned wrong status code")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_TOP_PROCESSES = JarTest()
failed: list = (
    JTT_APP_SYSTEM_TOP_PROCESSES.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_TOP_PROCESSES.run()
