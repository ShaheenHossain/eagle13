import eagle.tests
from eagle.tools import mute_logger


@eagle.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(eagle.tests.HttpCase):

    @mute_logger('eagle.addons.http_routing.models.ir_http', 'eagle.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
