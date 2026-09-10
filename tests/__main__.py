"""
JarTest
"""


from jarbin_toolkit_jartest import JarTest, Context, Show

# =========================================================
# IMPORT TESTS
# =========================================================

from tests import JT_makefile
from tests import JT_root


# =========================================================
# REGISTER TEST SUITE
# =========================================================

JTT_MAIN: JarTest = JarTest(
    context = Context(
        output = {
            "show_context": True,
            "show_output": True
        }
    )
)
failed: list = (
    JTT_MAIN.fetch()
    + JT_makefile.failed
    + JT_root.failed
)
JTT_MAIN.update_context()


if __name__ == '__main__':
    Show.failed_fetch(failed)
    JTT_MAIN.run()
