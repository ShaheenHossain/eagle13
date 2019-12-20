import eagle.tests
from eagle.tools import mute_logger


@eagle.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(eagle.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
