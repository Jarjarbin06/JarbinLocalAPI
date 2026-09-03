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

JTT_main: JarTest = JarTest()
JTT_main.fetch_tests()
JTT_main.run()
