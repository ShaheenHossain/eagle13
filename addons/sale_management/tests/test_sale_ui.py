import eagle.tests
# Part of Eagle. See LICENSE file for full copyright and licensing details.


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):

    def test_01_sale_tour(self):
        self.start_tour("/web", 'sale_tour', login="admin")
