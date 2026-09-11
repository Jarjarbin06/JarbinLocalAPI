from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_disk_get():
    url = "http://jarjarbin.local/api/system/disk"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(  response, body=False)

    Assertion.eq(response.status_code, 200, "API system disk returned wrong status code")

    for _type in ["usage", "partitions", "io"]:
        Assertion.contain(response.json(), _type, f"API system disk returned wrong response ({_type} not included)")

def JT_api_system_disk_get_per_category():
    base_url = "http://jarjarbin.local/api/system/disk?category={type}"

    for _type in ["usage", "partitions", "io"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        Assertion.eq(response.status_code, 200, f"API system disk returned wrong status code for type '{_type}'")
        Assertion.eq(list(response.json().keys())[0], _type, f"API system disk returned wrong response for type '{_type}'")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_DISK = JarTest()
failed: list = (
    JTT_API_SYSTEM_DISK.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_DISK.run()
