# Part of Eagle. See LICENSE file for full copyright and licensing details.

import eagle.tests


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):
    def test_admin(self):
        self.start_tour("/", 'blog', login='admin')
