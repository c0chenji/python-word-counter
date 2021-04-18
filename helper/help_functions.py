import string
import re


# Add top ten words and its number to the file
def add_qualified_words(target_file, target_list, top_flag):
    top_target = target_list[0][1]
    i = 0
    top_flag = top_flag-1

    while top_flag > 0:
        if target_list[i][1] != top_target:
            top_target = target_list[i][1]
            top_flag -= 1
        target_file.writelines("{} {} \n".format(
            target_list[i][0], target_list[i][1]))
        i += 1
    # Keep checking on the words that has same occcurence as the 10th word
    while i< len(target_list):
        if target_list[i][1] == top_target:
            target_file.writelines("{} {} \n".format(
                target_list[i][0], target_list[i][1]))
            i += 1
        else:
            break


# There are three ways to remove puncuation marks
# 1. Replace, and join methond, slowest, not efficient.
# 2. Regular regression, slower than translate method, but much faster than the first one
# 3. translate method in string library, fastest one.
# Note: string.punctuation contains most commonly used marks in a string
#       if string library is not allowed, we can  simply create a string to represent punctuation marks.
# Replace punctuation mark with space
def remove_punctuations(s):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    return s.translate(translator)

# # Alternative option,  use re library
# def remove_punctuations(s):
#     s = re.sub('['+string.punctuation+']', ' ', s)
#     return s


# A Normal merge sort function, but input is changed to a list of tuples
def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)


def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        # Since we are comparing the value of dictionary's item
        # and dictionary has been converted to a list of tuples
        # the index 1 of each element should be the required target

        if left_copy[left_copy_index][1] >= right_copy[right_copy_index][1]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest][1] > arr[l][1]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest][1] > arr[r][1]:
        largest = r
 
# The main function to sort an array of given size
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)