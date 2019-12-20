# -*- coding: utf-8 -*-

import eagle

def migrate(cr, version):
    registry = eagle.registry(cr.dbname)
    from eagle.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_in')
