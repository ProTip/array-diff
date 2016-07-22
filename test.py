import unittest
from protip import diff_arrays


class TestArrayDiff(unittest.TestCase):

    def verify_results(self, source, target, expectedAdds, expectedDels):
        adds, dels = diff_arrays(source, target)
        self.assertEqual(adds, expectedAdds)
        self.assertEqual(dels, expectedDels)

    def test_reference_input(self):
        self.verify_results(
            [1, 3, 5, 6, 8, 9],
            [1, 2, 5, 7, 9],
            [2, 7],
            [3, 6, 8])

    def test_last_items_compaired_at_same_time_and_different(self):
        self.verify_results(
            [1, 4],
            [1, 2],
            [2],
            [4])

    def test_last_items_compaired_at_same_time_after_duplicates(self):
        self.verify_results(
            [1, 2, 40, 40, 40, 40, 99],
            [5, 6, 7, 8, 40, 40, 98],
            [5, 6, 7, 8, 98],
            [1, 2, 40, 40, 99])

    def test_empty_arrays(self):
        self.verify_results([], [], [], [])

    def test_empty_target(self):
        self.verify_results([1], [], [], [1])

    def test_empty_source(self):
        self.verify_results([], [1], [1], [])

    def test_idetical_arrays(self):
        self.verify_results(
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [], [])

    def test_uneven_deplicates_at_end_less_in_current(self):
        self.verify_results(
            [1, 2, 3, 4, 5, 10, 10],
            [6, 7, 8, 10, 10, 10, 10],
            [6, 7, 8, 10, 10],
            [1, 2, 3, 4, 5])

    def test_uneven_deplicates_at_end_less_in_target(self):
        self.verify_results(
            [1, 2, 3, 10, 10, 10, 10],
            [4, 5, 6, 7, 8, 10, 10],
            [4, 5, 6, 7, 8],
            [1, 2, 3, 10, 10])

    def test_duplicates_in_middle_less_in_target(self):
        self.verify_results(
            [1, 2, 3, 20, 20, 20, 20, 50, 51, 52],
            [4, 5, 6, 7, 8, 9, 10, 11, 20, 20],
            [4, 5, 6, 7, 8, 9, 10, 11],
            [1, 2, 3, 20, 20, 50, 51, 52])

unittest.main()
