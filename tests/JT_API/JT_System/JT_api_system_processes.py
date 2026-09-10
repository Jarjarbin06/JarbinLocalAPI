from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_processes_get():
    url = "http://jarjarbin.local/api/system/processes"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)

    Assertion.eq(response.status_code, 200, "API system processes returned wrong status code")

    for _type in ["count", "pids", "processes"]:
        Assertion.contain(response.json(), _type, f"API system processes returned wrong response ({_type} not included)")

def JT_api_system_processes_get_per_category():
    base_url = "http://jarjarbin.local/api/system/processes?category={type}"

    for _type in ["count", "pids", "processes"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        if response.status_code != 200:
            Show.Response(response)
            Assertion(False, f"API system processes returned wrong status code for type '{_type}'")
            continue

        Assertion.eq(list(response.json().keys())[0], _type, f"API system processes returned wrong response for type '{_type}'")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_PROCESSES = JarTest()
failed: list = (
    JTT_API_SYSTEM_PROCESSES.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_PROCESSES.run()
