# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.
import eagle.tests


@eagle.tests.tagged('post_install', '-at_install')
class TestUi(eagle.tests.HttpCase):
    def test_01_portal_load_tour(self):
        self.start_tour("/", 'portal_load_homepage', login="portal")
