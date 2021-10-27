import unittest
from src.main import testeFunc


class TesteSoma(unittest.TestCase):
    def testeRetorno(self):
        self.assertEqual(testeFunc(10, 10), 20)
