# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pad_server = fields.Char(related='company_id.pad_server', string="Pad Server *", readonly=False)
    pad_key = fields.Char(related='company_id.pad_key', string="Pad Api Key *", readonly=False)
