import unittest
import asyncio


# def multiply_numbers(x, y):
#     return x * y

# class TestMultiplication(unittest.TestCase):
#     def test_multiply_two_positive_numbers(self):
#         result = multiply_numbers(2, 3)
#         self.assertEqual(result, 6)

#     def test_multiply_positive_and_negative_numbers(self):
#         result = multiply_numbers(2, -3)
#         self.assertEqual(result, -6)

#     def test_multiply_two_negative_numbers(self):
#         result = multiply_numbers(-2, -3)
#         self.assertEqual(result, 6)

#     def test_multiply_two_float_numbers(self):
#         result = multiply_numbers(2.5, 3.5)
#         self.assertEqual(result, 8.75)

#     def test_null(self):
#         result = multiply_numbers(5, 1)
#         self.assertNotEqual(result, 0)
        
class MyTest(unittest.TestCase):
    def setUp(self):
        self.my_list = [1, 2, 4]

    def tearDown(self):
        del self.my_list

    def test_list_length(self):
        self.assertEqual(len(self.my_list), 3)

    def test_list_contents(self):
        self.assertListEqual(self.my_list, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
