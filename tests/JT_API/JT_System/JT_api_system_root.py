from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_api_system_root_get():
    url = "http://jarjarbin.local/api/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)

    Assertion.eq(response.status_code, 200, "API system root returned wrong status code")

    for _type in ["cpu", "memory", "disk", "network", "processes", "sensors", "system"]:
        Assertion.contain(response.json(), _type, f"API system root returned wrong response ({_type} not included)")

def JT_api_system_root_get_per_type():
    base_url = "http://jarjarbin.local/api/system?type={type}"

    for _type in ["cpu", "memory", "disk", "network", "processes", "sensors", "system"]:
        url = base_url.format(type=_type)
        response = Get.HTTP.get(url, follow_redirects=True)

        Show.Request(response.request.method, url)

        if response.status_code != 200:
            Show.Response(response)
            Assertion(False, f"API system root returned wrong status code for type '{_type}'")
            continue

        Assertion.eq(list(response.json().keys())[0], _type, f"API system root returned wrong response for type '{_type}'")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_API.JT_System import JT_api_system_cpu
from tests.JT_API.JT_System import JT_api_system_disk
from tests.JT_API.JT_System import JT_api_system_memory
from tests.JT_API.JT_System import JT_api_system_network
from tests.JT_API.JT_System import JT_api_system_processes
from tests.JT_API.JT_System import JT_api_system_sensors
from tests.JT_API.JT_System import JT_api_system_system



# =========================================================
# REGISTER TEST
# =========================================================

JTT_API_SYSTEM_ROOT = JarTest()
failed: list = (
    JTT_API_SYSTEM_ROOT.fetch()
    + JT_api_system_cpu.failed
    + JT_api_system_memory.failed
    + JT_api_system_disk.failed
    + JT_api_system_network.failed
    + JT_api_system_processes.failed
    + JT_api_system_sensors.failed
    + JT_api_system_system.failed
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_API_SYSTEM_ROOT.run()
