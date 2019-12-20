# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import fields, models


class Product(models.Model):
    _inherit = "product.product"

    channel_ids = fields.One2many('slide.channel', 'product_id', string='Courses')
