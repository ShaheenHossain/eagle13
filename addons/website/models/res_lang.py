# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import api, models, tools, _
from eagle.addons.website.models import ir_http
from eagle.exceptions import UserError
from eagle.http import request


class Lang(models.Model):
    _inherit = "res.lang"

    def write(self, vals):
        if 'active' in vals and not vals['active']:
            if self.env['website'].search([('language_ids', 'in', self._ids)]):
                raise UserError(_("Cannot deactivate a language that is currently used on a website."))
        return super(Lang, self).write(vals)

    @api.model
    @tools.ormcache_context(keys=("website_id",))
    def get_available(self):
        """ Return the available languages as a list of (code, name) sorted by name. """
        website = ir_http.get_request_website()
        if website:
            return sorted([(lang.code, lang.url_code, lang.name) for lang in request.website.language_ids])
        return super(Lang, self).get_available()
