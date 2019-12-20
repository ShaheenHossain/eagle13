# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import http
from eagle.http import request
from eagle.addons.portal.controllers.portal import CustomerPortal


class CustomerPortal(CustomerPortal):

    @http.route(["/sale_quotation_builder/template/<model('sale.order.template'):template>"], type='http', auth="user", website=True)
    def sale_quotation_builder_template_view(self, template, **post):
        values = {'template': template}
        return request.render('sale_quotation_builder.so_template', values)
