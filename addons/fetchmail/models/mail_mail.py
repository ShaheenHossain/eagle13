# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import fields, models


class MailMail(models.Model):
    _inherit = 'mail.mail'

    fetchmail_server_id = fields.Many2one('fetchmail.server', "Inbound Mail Server", readonly=True, index=True)
