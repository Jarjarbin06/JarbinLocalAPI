from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_updater_root_get():
    url = "http://jarjarbin.local/updater"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Updater root returned wrong status code")
    Assertion.eq(response.json()["data"], {"message": "Hello World!"}, "Updater root returned wrong response")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_UPDATER = JarTest()
failed: list = (
    JTT_UPDATER.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_UPDATER.run()
