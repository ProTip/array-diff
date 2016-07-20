import unittest
from protip import diff_arrays


class TestArrayDiff(unittest.TestCase):

    def test_reference_input(self):
        adds, dels = diff_arrays(
            [1, 3, 5, 6, 8, 9],
            [1, 2, 5, 7, 9])
        self.assertEqual(adds, [2, 7])
        self.assertEqual(dels, [3, 6, 8])

    def test_last_items_compaired_at_same_time_and_different(self):
        adds, dels = diff_arrays(
            [1, 4],
            [1, 2])
        self.assertEqual(adds, [2])
        self.assertEqual(dels, [4])

    def test_last_items_compaired_at_same_time_after_duplicates(self):
        adds, dels = diff_arrays(
            [1, 2, 40, 40, 40, 40, 99],
            [5, 6, 7, 8, 40, 40, 98])
        self.assertEqual(adds, [5, 6, 7, 8, 98])
        self.assertEqual(dels, [1, 2, 40, 40, 99])

    def test_empty_arrays(self):
        adds, dels = diff_arrays([], [])
        self.assertEqual(adds, dels, [])

    def test_idetical_arrays(self):
        adds, dels = diff_arrays(
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5])
        self.assertEqual(adds, dels, [])

    def test_uneven_deplicates_at_end_less_in_current(self):
        adds, dels = diff_arrays(
            [1, 2, 3, 4, 5, 10, 10],
            [6, 7, 8, 10, 10, 10, 10]
        )
        self.assertEqual(adds, [6, 7, 8, 10, 10])
        self.assertEqual(dels, [1, 2, 3, 4, 5])

    def test_uneven_deplicates_at_end_less_in_target(self):
        adds, dels = diff_arrays(
            [1, 2, 3, 10, 10, 10, 10],
            [4, 5, 6, 7, 8, 10, 10],
        )
        self.assertEqual(adds, [4, 5, 6, 7, 8])
        self.assertEqual(dels, [1, 2, 3, 10, 10])

    def test_duplicates_in_middle_less_in_target(self):
        adds, dels = diff_arrays(
            [1, 2, 3, 20, 20, 20, 20, 50, 51, 52],
            [4, 5, 6, 7, 8, 9, 10, 11, 20, 20]
        )
        self.assertEqual(adds, [4, 5, 6, 7, 8, 9, 10, 11])
        self.assertEqual(dels, [1, 2, 3, 20, 20, 50, 51, 52])

unittest.main()
