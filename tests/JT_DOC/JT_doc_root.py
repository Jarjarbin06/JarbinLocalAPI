from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_doc_root_get():
    url = "http://jarjarbin.local/doc"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "Doc returned wrong status code")
    Assertion.contain(response.text, "📦 JarbinLocalAPI — Route Reference", "Doc returned wrong response")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_DOC import JT_doc_documentations


# =========================================================
# REGISTER TEST
# =========================================================

JTT_DOC = JarTest()
failed: list = (
    JTT_DOC.fetch()
    + JT_doc_documentations.failed
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_DOC.run()
