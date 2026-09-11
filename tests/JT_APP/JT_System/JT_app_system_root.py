from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_app_system_root_get():
    url = "http://jarjarbin.local/app/system"

    response = Get.HTTP.get(url, follow_redirects=True)

    Show.Request(response.request.method, url)
    Show.Response(response, body=False)

    Assertion.eq(response.status_code, 200, "APP system root returned wrong status code")


# =========================================================
# IMPORT TESTS
# =========================================================

from tests.JT_APP.JT_System import JT_app_system_battery
from tests.JT_APP.JT_System import JT_app_system_cpu
from tests.JT_APP.JT_System import JT_app_system_disk
from tests.JT_APP.JT_System import JT_app_system_memory
from tests.JT_APP.JT_System import JT_app_system_network
from tests.JT_APP.JT_System import JT_app_system_processes
from tests.JT_APP.JT_System import JT_app_system_system
from tests.JT_APP.JT_System import JT_app_system_temperatures
from tests.JT_APP.JT_System import JT_app_system_top_processes



# =========================================================
# REGISTER TEST
# =========================================================

JTT_APP_SYSTEM_ROOT = JarTest()
failed: list = (
        JTT_APP_SYSTEM_ROOT.fetch()
        + JT_app_system_battery.failed
        + JT_app_system_cpu.failed
        + JT_app_system_disk.failed
        + JT_app_system_memory.failed
        + JT_app_system_network.failed
        + JT_app_system_processes.failed
        + JT_app_system_system.failed
        + JT_app_system_temperatures.failed
        + JT_app_system_top_processes.failed
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_APP_SYSTEM_ROOT.run()
