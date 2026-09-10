from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_memory_get():
    url = "http://jarjarbin.local/api/system/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)

    Assertion.eq(response.status_code, 200, "API system system returned wrong status code")

    for _type in ["boot_time", "users"]:
        Assertion.contain(response.json(), _type, f"API system system returned wrong response ({_type} not included)")

def JT_api_system_memory_get_per_category():
    base_url = "http://jarjarbin.local/api/system/system?category={type}"

    for _type in ["boot_time", "users"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        if response.status_code != 200:
            Show.Response(response)
            Assertion(False, f"API system system returned wrong status code for type '{_type}'")
            continue

        Assertion.eq(list(response.json().keys())[0], _type, f"API system system returned wrong response for type '{_type}'")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_SYSTEM = JarTest()
failed: list = (
    JTT_API_SYSTEM_SYSTEM.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_SYSTEM.run()
