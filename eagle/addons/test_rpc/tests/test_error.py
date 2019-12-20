# -*- coding: utf-8 -*-

from functools import partial

from eagle.tests import common
from eagle.tools.misc import mute_logger


class TestError(common.HttpCase):
    def setUp(self):
        super(TestError, self).setUp()
        uid = self.ref("base.user_admin")
        self.rpc = partial(self.xmlrpc_object.execute, common.get_db_name(), uid, "admin")

        # Reset the admin's lang to avoid breaking tests due to admin not in English
        self.rpc("res.users", "write", [uid], {"lang": False})

    def test_01_create(self):
        """ Create: mandatory field not provided """
        self.rpc("test_rpc.model_b", "create", {"name": "B1"})
        try:
            with mute_logger("eagle.sql_db"):
                self.rpc("test_rpc.model_b", "create", {})
            raise
        except Exception as e:
            self.assertIn("The operation cannot be completed:", e.faultString)
            self.assertIn("Create/update: a mandatory field is not set.", e.faultString)
            self.assertIn(
                "Delete: another model requires the record being deleted. If possible, archive it instead.",
                e.faultString,
            )
            self.assertIn("Model: Model B (test_rpc.model_b), Field: Name (name)", e.faultString)

    def test_02_delete(self):
        """ Delete: NOT NULL and ON DELETE RESTRICT constraints """
        b1 = self.rpc("test_rpc.model_b", "create", {"name": "B1"})
        b2 = self.rpc("test_rpc.model_b", "create", {"name": "B2"})
        self.rpc("test_rpc.model_a", "create", {"name": "A1", "field_b1": b1, "field_b2": b2})

        try:
            with mute_logger("eagle.sql_db"):
                self.rpc("test_rpc.model_b", "unlink", b1)
            raise
        except Exception as e:
            self.assertIn("The operation cannot be completed:", e.faultString)
            self.assertIn(
                "another model requires the record being deleted. If possible, archive it instead.",
                e.faultString,
            )
            self.assertIn(
                "Model: Model A (test_rpc.model_a), Constraint: test_rpc_model_a_field_b1_fkey",
                e.faultString,
            )

        # Unlink b2 => ON DELETE RESTRICT constraint raises
        try:
            with mute_logger("eagle.sql_db"):
                self.rpc("test_rpc.model_b", "unlink", b2)
            raise
        except Exception as e:
            self.assertIn("The operation cannot be completed:", e.faultString)
            self.assertIn(
                " another model requires the record being deleted. If possible, archive it instead.",
                e.faultString,
            )
            self.assertIn(
                "Model: Model A (test_rpc.model_a), Constraint: test_rpc_model_a_field_b2_fkey",
                e.faultString,
            )
