from src.components import PieceSide
import unittest

class TestPieceSide(unittest.TestCase):
    def test_enum_is_right(self):
        self.assertEqual(PieceSide.WHITE, 1)
        self.assertEqual(PieceSide.BLACK, -1)

