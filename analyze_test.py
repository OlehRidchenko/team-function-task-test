import unittest
from analyze import analyze_numbers


class TestAnalyzeNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(analyze_numbers([]), {
            "sum": 0,
            "average": None,
            "maximum": None,
            "minimum": None,
            "even_count": 0,
            "odd_count": 0
        })

    def test_positive_numbers(self):
        result = analyze_numbers([1, 2, 3, 4, 5])
        self.assertEqual(result["sum"], 15)
        self.assertEqual(result["average"], 3)
        self.assertEqual(result["maximum"], 5)
        self.assertEqual(result["minimum"], 1)
        self.assertEqual(result["even_count"], 2)
        self.assertEqual(result["odd_count"], 3)

    def test_negative_numbers(self):
        result = analyze_numbers([-1, -2, -3, -4])
        self.assertEqual(result["sum"], -10)
        self.assertEqual(result["average"], -2.5)
        self.assertEqual(result["maximum"], -1)
        self.assertEqual(result["minimum"], -4)
        self.assertEqual(result["even_count"], 2)
        self.assertEqual(result["odd_count"], 2)

    def test_numbers_with_zero(self):
        result = analyze_numbers([0, 1, 2, 3])
        self.assertEqual(result["sum"], 6)
        self.assertEqual(result["average"], 1.5)
        self.assertEqual(result["maximum"], 3)
        self.assertEqual(result["minimum"], 0)
        self.assertEqual(result["even_count"], 2)
        self.assertEqual(result["odd_count"], 2)

    def test_all_even_numbers(self):
        result = analyze_numbers([2, 4, 6, 8])
        self.assertEqual(result["even_count"], 4)
        self.assertEqual(result["odd_count"], 0)

    def test_all_odd_numbers(self):
        result = analyze_numbers([1, 3, 5, 7])
        self.assertEqual(result["even_count"], 0)
        self.assertEqual(result["odd_count"], 4)

    def test_single_number(self):
        result = analyze_numbers([7])
        self.assertEqual(result["sum"], 7)
        self.assertEqual(result["average"], 7)
        self.assertEqual(result["maximum"], 7)
        self.assertEqual(result["minimum"], 7)
        self.assertEqual(result["even_count"], 0)
        self.assertEqual(result["odd_count"], 1)

    def test_duplicate_numbers(self):
        result = analyze_numbers([5, 5, 2, 2])
        self.assertEqual(result["sum"], 14)
        self.assertEqual(result["average"], 3.5)
        self.assertEqual(result["maximum"], 5)
        self.assertEqual(result["minimum"], 2)
        self.assertEqual(result["even_count"], 2)
        self.assertEqual(result["odd_count"], 2)


    def test_large_numbers(self):
        result = analyze_numbers([1000, 2000, 3000])
        self.assertEqual(result["sum"], 6000)
        self.assertEqual(result["average"], 2000)
        self.assertEqual(result["maximum"], 3000)
        self.assertEqual(result["minimum"], 1000)
        self.assertEqual(result["even_count"], 3)
        self.assertEqual(result["odd_count"], 0)

    def test_mixed_positive_and_negative_numbers(self):
        result = analyze_numbers([-5, -2, 3, 4])
        self.assertEqual(result["sum"], 0)
        self.assertEqual(result["average"], 0)
        self.assertEqual(result["maximum"], 4)
        self.assertEqual(result["minimum"], -5)
        self.assertEqual(result["even_count"], 2)
        self.assertEqual(result["odd_count"], 2)

if __name__ == "__main__":
    unittest.main()
