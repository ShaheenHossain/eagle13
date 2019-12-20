# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import http
from eagle.http import request


class ImSupport(http.Controller):

    @http.route('/im_support/tests', type='http', auth="user")
    def test_suite(self, mod=None, **kwargs):
        return request.render('im_support.support_qunit_suite')
