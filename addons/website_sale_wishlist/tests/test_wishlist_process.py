# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.
import eagle.tests


@eagle.tests.common.at_install(False)
@eagle.tests.common.post_install(True)
class TestUi(eagle.tests.HttpCase):
    def test_01_wishlist_tour(self):
        self.start_tour("/", 'shop_wishlist')
