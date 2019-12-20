import eagle.tests
# Part of Eagle. See LICENSE file for full copyright and licensing details.


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):
    def test_01_event_configurator(self):
        self.start_tour("/web", 'event_configurator_tour', login="admin")
