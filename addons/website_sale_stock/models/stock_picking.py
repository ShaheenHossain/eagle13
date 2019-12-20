# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import models, api, fields
from eagle.tools.translate import _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    website_id = fields.Many2one('website', related='sale_id.website_id', string='Website',
                                 help='Website this picking belongs to.',
                                 store=True, readonly=True)

