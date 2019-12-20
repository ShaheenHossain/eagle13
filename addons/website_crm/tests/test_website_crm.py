# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

import eagle.tests


@eagle.tests.tagged('post_install', '-at_install')
class TestWebsiteCrm(eagle.tests.HttpCase):

    def test_tour(self):
        self.start_tour("/", 'website_crm_tour')

        # check result
        record = self.env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        self.assertEqual(len(record), 1)
        self.assertEqual(record.contact_name, 'John Smith')
        self.assertEqual(record.email_from, 'john@smith.com')
        self.assertEqual(record.partner_name, 'Eagle ERP')
