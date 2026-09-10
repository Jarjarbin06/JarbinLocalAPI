from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_sensors_get():
    url = "http://jarjarbin.local/api/system/sensors"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)

    Assertion.eq(response.status_code, 200, "API system sensors returned wrong status code")

    for _type in ["temperatures", "fans", "battery"]:
        Assertion.contain(response.json(), _type, f"API system sensors returned wrong response ({_type} not included)")

def JT_api_system_sensors_get_per_category():
    base_url = "http://jarjarbin.local/api/system/sensors?category={type}"

    for _type in ["temperatures", "fans", "battery"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        if response.status_code != 200:
            Show.Response(response)
            Assertion(False, f"API system sensors returned wrong status code for type '{_type}'")
            continue

        Assertion.eq(list(response.json().keys())[0], _type, f"API system sensors returned wrong response for type '{_type}'")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_SENSORS = JarTest()
failed: list = (
    JTT_API_SYSTEM_SENSORS.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_SENSORS.run()
