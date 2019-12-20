# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

import eagle
import eagle.exceptions

def login(db, login, password):
    res_users = eagle.registry(db)['res.users']
    try:
        return res_users._login(db, login, password)
    except eagle.exceptions.AccessDenied:
        return False

def check(db, uid, passwd):
    res_users = eagle.registry(db)['res.users']
    return res_users.check(db, uid, passwd)

def compute_session_token(session, env):
    self = env['res.users'].browse(session.uid)
    return self._compute_session_token(session.sid)

def check_session(session, env):
    self = env['res.users'].browse(session.uid)
    expected = self._compute_session_token(session.sid)
    if expected and eagle.tools.misc.consteq(expected, session.session_token):
        return True
    self._invalidate_session_cache()
    return False
