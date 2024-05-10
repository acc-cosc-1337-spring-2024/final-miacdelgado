#write function tests here, don't add input('') statements here!
import unittest

# Test cases for question a
from src.question_a.question_a import lowest_number, highest_number, total, average

class Test_Config(unittest.TestCase):
    def test_question_a_lowest_number(self):
        list_num = [10, 20, 30, 40, 50]
        self.assertEqual(lowest_number(list_num), 10)

    def test_question_a_highest_number(self):
        list_num = [10, 20, 30, 40, 50]
        self.assertEqual(highest_number(list_num), 50)

    def test_question_a_total(self):
        list_num = [10, 20, 30, 40, 50]
        self.assertEqual(total(list_num), 150)

    def test_question_a_average(self):
        list_num = [10, 20, 30, 40, 50]
        self.assertEqual(average(list_num), 30)