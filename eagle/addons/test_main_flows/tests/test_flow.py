# Part of Eagle. See LICENSE file for full copyright and licensing details.

import eagle.tests


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):

    def test_01_main_flow_tour(self):
        self.start_tour("/web", 'main_flow_tour', login="admin", timeout=180)
