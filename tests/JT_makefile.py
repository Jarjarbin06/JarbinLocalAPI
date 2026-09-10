from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show


# =========================================================
# TESTS
# =========================================================

def JT_makefile_status_not_running():
    out, err, code = Get.Redirect.cmd_all_std("make --no-print-directory status")

    Show(out.strip())

    Assertion.eq(code, 0)
    Assertion.contain(out, "not running")
    Assertion.eq(err, "")

def JT_makefile_start():
    out, err, code = Get.Redirect.cmd_all_std("make --no-print-directory start")

    Show(out.strip())

    Assertion.eq(code, 0)
    Assertion.contain(out, "started")
    Assertion.eq(err, "")

def JT_makefile_status_running():
    out, err, code = Get.Redirect.cmd_all_std("make --no-print-directory status")

    Show(out.strip())

    Assertion.eq(code, 0)
    Assertion.ncontain(out, "not running")
    Assertion.eq(err, "")

def JT_makefile_stop():
    out, err, code = Get.Redirect.cmd_all_std("make --no-print-directory stop")

    Show(out.strip())

    Assertion.eq(code, 0)
    Assertion.contain(out, "stopped")
    Assertion.eq(err, "")


# =========================================================
# REGISTER TEST
# =========================================================

JTT_MAKEFILE = JarTest()
failed: list = (
    JTT_MAKEFILE.fetch()
)


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_MAKEFILE.run()
