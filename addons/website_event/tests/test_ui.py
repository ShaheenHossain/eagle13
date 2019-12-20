import eagle.tests


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):
    def test_admin(self):
        self.start_tour("/", 'event', login='admin')
