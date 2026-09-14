from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_doc_get_root():
    url = "http://jarjarbin.local/doc/root"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Doc returned wrong status code")
    Assertion.contain(response.text, "GET /", "Doc returned wrong response")


def JT_doc_get_api():
    url = "http://jarjarbin.local/doc/api"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Doc returned wrong status code")
    Assertion.contain(response.text, "GET /api", "Doc returned wrong response")


def JT_doc_get_api_system():
    url = "http://jarjarbin.local/doc/api/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Doc returned wrong status code")
    Assertion.contain(response.text, "GET /api/system", "Doc returned wrong response")


def JT_doc_get_api_system_cpu():
    url = "http://jarjarbin.local/doc/api/system/cpu"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Doc returned wrong status code")
    Assertion.contain(response.text, "GET /api/system/cpu", "Doc returned wrong response")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_DOC_DOCUMENTATIONS = JarTest()
failed: list = (
    JTT_DOC_DOCUMENTATIONS.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_DOC_DOCUMENTATIONS.run()
