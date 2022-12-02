import unittest

from typecho_password import PasswordContext


class TestContext(unittest.TestCase):
    def test_verify(self):
        m = PasswordContext()
        password = "123456789ABCabc"

        self.assertTrue(m.verify(password, "$P$BguashH7i1s/SbYbNt3MnFrK8pjNe0/"))

        self.assertFalse(m.verify(password, "$P$BguashH7i1s/SbYbNt3MnFrK8pjNe1/"))
        self.assertFalse(m.verify(password, "$P$Bgu"))

    def test_hash(self):
        m = PasswordContext()
        password = "123456789ABCabc"
        hashed_password = m.hash(password)

        self.assertTrue(m.hash(password) != hashed_password)
        self.assertTrue(m.verify(password, hashed_password))