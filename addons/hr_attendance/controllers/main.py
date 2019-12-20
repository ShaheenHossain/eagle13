# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import http
from eagle.http import request


class HrAttendance(http.Controller):
    @http.route('/hr_attendance/kiosk_keepalive', auth='user', type='json')
    def kiosk_keepalive(self):
        request.httprequest.session.modified = True
        return {}
