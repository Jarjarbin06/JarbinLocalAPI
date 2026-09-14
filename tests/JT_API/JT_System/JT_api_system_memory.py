from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_memory_get():
    url = "http://jarjarbin.local/api/system/memory"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(  response, body=False)

    Assertion.eq(response.status_code, 200, "API system memory returned wrong status code")

    for _type in ["virtual", "swap"]:
        Assertion.contain(response.json()["data"], _type, f"API system memory returned wrong response ({_type} not included)")

def JT_api_system_memory_get_per_category():
    base_url = "http://jarjarbin.local/api/system/memory?category={type}"

    for _type in ["virtual", "swap"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        Assertion.eq(response.status_code, 200, f"API system memory returned wrong status code for type '{_type}'")
        Assertion.eq(list(response.json()["data"].keys())[0], _type, f"API system memory returned wrong response for type '{_type}'")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_MEMORY = JarTest()
failed: list = (
    JTT_API_SYSTEM_MEMORY.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_MEMORY.run()
