from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_network_get():
    url = "http://jarjarbin.local/app/system/network"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "APP system network returned wrong status code")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_NETWORK = JarTest()
failed: list = (
    JTT_APP_SYSTEM_NETWORK.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_NETWORK.run()
