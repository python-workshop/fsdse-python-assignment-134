from unittest import TestCase
from bst import Node


class TestBstHeight(TestCase):
    def test_height(self):
        try:
            from build import BstHeight
        except ImportError:
            self.assertFalse("no function found")


        bst = BstHeight(Node(5))
        self.assertEqual(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        self.assertEqual(bst.height(bst.root), 3)

