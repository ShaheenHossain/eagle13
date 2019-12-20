# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(Http, self).session_info()
        if self.env.user.has_group('base.group_user'):
            res['eaglebot_initialized'] = self.env.user.eaglebot_state != 'not_initialized'
        return res
