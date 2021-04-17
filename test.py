import unittest
from word_counter import InputFile, GetOutput
from helper.help_functions import *

# Test sorting function for dictionary/list of tuple
# The results of testing merge_sort and heap_sort are pretty same, I choose mersort here


class dict_sort_test(unittest.TestCase):

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


class remove_punctuations_test(unittest.TestCase):
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

class InputFile_test(unittest.TestCase):
    def test_none_existing_file(self):
        fakeInput ="abc.txt"
        target = InputFile(fakeInput)
        
        


if __name__ == '__main__':
    unittest.main()
