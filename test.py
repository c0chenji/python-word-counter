import unittest

from word_counter import InputFile, GetOutput
from helper.help_functions import *
from unittest.mock import patch, mock_open


class DictSortTest(unittest.TestCase):
    """Test sorting function for dictionary/list of tuple
       The results of testing merge_sort and heap_sort are pretty same, I choose mersort here
    """

    def sort(self, lst):
        copy = lst[:]
        merge_sort(copy, 0, len(copy) - 1)
        return copy

    def test_empty_list(self):
        lst = []
        sorted_lst = self.sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_single_item(self):
        lst = [("a", 1)]
        sorted_lst = self.sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_two_items_unsorted(self):
        lst = [("b", 1), ("a", 3)]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [("a", 3), ("b", 1)])

    def test_odd_number_of_items(self):
        lst = [("Hi", 13), ("Hello", 7), ("Hola", 15)]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [("Hola", 15), ("Hi", 13), ("Hello", 7)])

    def test_even_number_of_items(self):
        lst = [("Hi", 13), ("Hello", 7), ("Hola", 15), ("Bonjur", 12)]
        sorted_lst = self.sort(lst)
        self.assertEqual(
            sorted_lst, [("Hola", 15), ("Hi", 13), ("Bonjur", 12), ("Hello", 7)])

    def test_duplicate_integers_in_list(self):
        lst = [("Hi", 13), ("Hello", 700), ("Hola", 50000), ("Bonjur", 7)]
        sorted_lst = self.sort(lst)
        self.assertEqual(
            sorted_lst, [("Hola", 50000), ("Hello", 700), ("Hi", 13),  ("Bonjur", 7)])


class RemovePunctuationsTest(unittest.TestCase):
    # Tests for replacing punctuations with spaces from a string
    def clean(self, target):
        copy = remove_punctuations(target[:])
        return copy

    def test_empty_string(self):
        target = " "
        result = self.clean(target)
        self.assertEqual(result, target)

    def test_one_puncs_in_string(self):
        target = " a@"
        result = self.clean(target)
        self.assertEqual(result, " a ")

    def test_multiple_puncs_string(self):
        target = "I just 'want to,remove _+#$@1!$%^&punctuations."
        result = self.clean(target)
        self.assertEqual(
            result, "I just  want to remove      1     punctuations ")


class InputTest(unittest.TestCase):
    # Tests for total word counter and dictionary result.
    def test_empty_file(self):
        target = InputFile(r".\txt_for_test\empty_input.txt")
        dict_result = target.count_and_save()
        self.assertEqual(target.total_words, 0)
        self.assertEqual(len(target.occurence_set),0)
        self.assertEqual(dict_result,{})

        # # Another way, using mock
        # with patch('word_counter.open', mock_open(read_data='')) as m:
        #     target = InputFile("fake_empty_input")
        #     dict_result = target.count_and_save()
        # self.assertEqual(target.total_words, 0)
        # self.assertEqual(len(target.occurence_set), 0)
        # self.assertEqual(dict_result, {})


    def test_one_line_file(self):
        target = InputFile(r".\txt_for_test\one_line.txt")
        dict_result = target.count_and_save()
        self.assertEqual(target.total_words, 10)
        self.assertEqual(len(target.occurence_set),4)
        self.assertEqual(dict_result,{"one":1, "two":2,"three":3,"four":4})

        # # Another way, using mock
        # input_content = """ one two- Two" three Three'three *(&*&*(&(*&(four- four  four- four """
        # with patch('word_counter.open', mock_open(read_data=input_content)) as m:
        #     target = InputFile("fake_one_line_input")
        #     dict_result = target.count_and_save()
        # self.assertEqual(target.total_words, 10)
        # self.assertEqual(len(target.occurence_set), 4)
        # self.assertEqual(
        #     dict_result, {"one": 1, "two": 2, "three": 3, "four": 4})

    def test_multiple_line_file(self):
        target = InputFile(r".\txt_for_test\multiple_lines.txt")
        dict_result = target.count_and_save()
        self.assertEqual(target.total_words, 66)
        self.assertEqual(len(target.occurence_set),11)
        self.assertEqual(dict_result,{"one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11})

        # # Another way using mock
        # input_content = """ one two- Two" three Three'three   four- four  four- four\n
        #                     five-five-five-five-five\n
        #                     six six six six six six\n
        #                     seven seven seven seven seven seven seven\n
        #                     eight eight eight eight eight eight eight eight\n
        #                     nine/nine/nine/nine/nine/nine/nine/nine/nine/\n
        #                     ten ten ten ten ten ten ten ten ten ten\n
        #                     eleven eleven eleven eleven eleven eleven eleven eleven eleven eleven eleven  """
        # with patch('word_counter.open', mock_open(read_data=input_content)) as m:
        #     target = InputFile("fake_one_line_input")
        #     dict_result = target.count_and_save()
        #     dict_result = target.count_and_save()
        # self.assertEqual(target.total_words, 66)
        # self.assertEqual(len(target.occurence_set),11)
        # self.assertEqual(dict_result,{"one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11})


class OutputTest(unittest.TestCase):
    # This program is running on windows, the directory formats should be changed if you are using linux.
    # Tests for checking if output files are created correctly.
    def test_empty_file(self):
        target = GetOutput(r".\txt_for_test\empty_input.txt",
                           r".\txt_for_test\empty_output.txt").sorted_and_save()
        expect_result = ["There is no word in this file."]
        with open(r".\txt_for_test\empty_output.txt", "r") as f:
            actual_result = f.readlines()

        self.assertEqual(expect_result, actual_result)

    def test_one_line_file(self):
        target = GetOutput(r".\txt_for_test\one_line.txt",
                           r".\txt_for_test\one_line_output.txt").sorted_and_save()
        expect_result = ["Top 4 Words: \n", "four 4 \n",
                         "three 3 \n", "two 2 \n", "one 1 \n", "Total Words: 10"]
        with open(r".\txt_for_test\one_line_output.txt", "r") as f:
            actual_result = f.readlines()
        self.assertEqual(expect_result, actual_result)

    def test_multiple_line_file(self):
        target = GetOutput(r".\txt_for_test\multiple_lines.txt",
                           r".\txt_for_test\multiple_lines_output.txt").sorted_and_save()
        expect_result = ["Top 10 Words: \n",
                         "eleven 11 \n",
                         "ten 10 \n",
                         "nine 9 \n",
                         "eight 8 \n",
                         "seven 7 \n",
                         "six 6 \n",
                         "five 5 \n",
                         "four 4 \n",
                         "three 3 \n",
                         "two 2 \n",
                         "Total Words: 66"
                         ]
        with open(r".\txt_for_test\multiple_lines_output.txt", "r") as f:
            actual_result = f.readlines()
        self.assertEqual(expect_result, actual_result)

    def test_special_case_file(self):
        # a case with more than 10 items in the top-ten list
        target = GetOutput(r".\txt_for_test\special_case.txt",
                           r".\txt_for_test\special_case_output.txt").sorted_and_save()
        expect_result = ["Top 10 Words: \n",
                         "eleven 11 \n",
                         "ten 10 \n",
                         "nine 9 \n",
                         "eight 8 \n",
                         "seven 7 \n",
                         "six 6 \n",
                         "five 5 \n",
                         "four 4 \n",
                         "three 3 \n",
                         "one 2 \n",
                         "two 2 \n",
                         "Total Words: 67"
                         ]
        with open(r".\txt_for_test\special_case_output.txt", "r") as f:
            actual_result = f.readlines()
        self.assertEqual(expect_result, actual_result)


if __name__ == '__main__':
    unittest.main()
