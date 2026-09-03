"""
JarTest
"""


from jarbin_toolkit_jartest import JarTest, Get, Assertion, Show, Benchmark


# =========================================================
# IMPORT TESTS
# =========================================================

from tests import JT_root
from tests.JT_API import JT_api_root
from tests.JT_APP import JT_app_root


# =========================================================
# REGISTER TEST SUITE
# =========================================================

JTT_MAIN: JarTest = JarTest()
JTT_MAIN.fetch_tests()
JTT_MAIN.run()
