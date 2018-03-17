import unittest
from index import f


class TestClassF(unittest.TestCase):
    def test_f(self):
        assert (f())
