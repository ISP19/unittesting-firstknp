import unittest
from listutil import unique

class CountUnique(unittest.TestCase):
    def test_empty_item_list(self):
        self.assertListEqual([], unique([]))
    def test_one_item_list(self):
        self.assertListEqual(['one'], unique(['one']))
        self.assertListEqual([1], unique([1]))
        self.assertListEqual([1], unique([1, 1, 1, 1]))
    def test_extreamcase(self):
        self.assertListEqual([1, 2, 3, 4, 5], unique([1, 2, 3, 4, 5]))
        self.assertListEqual(['one', 'two'], unique(['one', 'two', 'two', 'two']))
        self.assertListEqual([6, 1, 0, 5, 4, 3], unique([6, 1, 1, 0, 5, 4, 5, 4, 3, 1]))

if __name__ == '__main__':
    unittest.main()