## Python word-counter
A python word counter, counts words in text files.

---
## Table of contents
* [General Info](#general-info)
* [Project Structure](#project-structure)
* [Technologies](#technologies)
* [Installation](#installation)
* [Scenarios](#scenarios)
* [Usage](#usage)
* [Test](#test)

---
## General Info
A simple application that takes a UTF-8 plain-text file as input and outputs:  
* Total number of words in text file  
* Ten most common words and number of occurrences for each


---
## Technologies
Project is created with:
* python 3.9.1

---
## Project Structure
    .
    ├── helper                       # Helper function folder
    │   ├── helper_functions.py  
    ├── txt_for_test                 # Folder of text files for testing
    ├── test.py                      # Unittest  
    ├── word_counter.py
    ├── input.txt                    # Should be created before running the program
    ├── output.txt
    └── README.md
---
## Installation

Follow the [instruction](https://wiki.python.org/moin/BeginnersGuide/Download) to install python3.  

---
## Scenarios
#### Data structure:
In this project, **dictionary** is used to store words as keys, and their number of occurrences as values.  

**pros:** 
* Ideal data type for counting and saving words and number of occurrences.
* lookups in dictionaries are O(1) by requiring that key objects provide a "hash" function.

**cons:**  
* Built-in sorting is not allowed, and we can not access dictionary items by index, then converting items of the dictionary into a list of tuples would be a choice for sorting. 

#### Sorting methods: 
* **QuickSort**: Faster than MergeSort and HeapSort, but its worst-case complexity is O(n^2), and it is not stable.  
* **MergeSort**: Slightly faster than HeapSort for larger sets, but it requires more memory than HeapSort does.  
* **HeapSort**: Slowest of the O(nlog n) sorting algorithms, but it is a memory-saving sorting since it doesn't require massive recursion or multiple arrays to work. 
 
In this project, I will select **MergeSort** to implement the sorting.

The target we need to sort would be converted into:  
```python
[("The",12),("They",2),("Their",20)]
```  
Then the second element in each item would be the target we need to do the comparison.

#### Punctuations removal:  
I got two ways to handle punctuations removal.  
* Use translate() and maketrans() of "string" library to replace punctuations with spaces in a string.  
* Use re.sub() of "re" library to handle the replacement, but it is slower than the previous method.
* Using join() and replace() is also a solution, but it is much slower than the previous two methods.  

#### Inputs cases: 
A UTF-8 plain-text file of words and punctuations. However, there are multiple cases we need to consider based on each string line.

* **Case 1**:  
If the string is organized and formatted as below:
```python
"Go home!" he said.
```
Then we simply use split() to separate words into a list, then remove punctuation for each word.
* **Case 2**:  
If the string is unorganized and unformatted as below:
```python
"Go,home!" the-boss said.
```
Normal word-counter would count words surrounding by two spaces as individuals.  
(e.g., it would be 3 words in MS office doc for this case)  
It makes non-sense in the real-world scenario, there are actually 5 words since the-boss is consists of 2 words.  
For this case, I will replace punctuations with spaces first, then split them into a list of strings without spaces.

* **Case 3**:  
If the string is extremely unformated and complicated as below:  
```python
"Go,'G8, you lost your$8,888.01!" the-boss stoped&said.
```
According to the definitions, **"G8"** is the abbreviation for the Group of Eight(4 words), then it should not be counted as a word.  
**$8,888.01** is literally a number, it is not a word either. In addtion, it is hard to process strings like "your$8,888.01!"(maybe regexp could help) without third party libraries.
To implement this case, the installation of multiple third-party libraries like vocabulary-checker is required(It is violating the rule of this project). Hence I will not consider this case in this project.


Therefore, I will consider the data of input are reasonable words like **case 2** (abbreviations and numbers should not be counted).



#### Outputs cases:  
* **Case 1**:  
If "**Top ten words**" are simply referred to the first ten elements of a selected list, then the problem would be solved by getting the first ten elements in the list.
* **Case 2**:  
If our goal is to list top_ten words based on the number of their occurrences, the result could be more than ten elements.   
e.g., {"Hello":100, "Hi":90, "Hola":90}  
There are three words that should be on the result list, but they would be counted as the top two words since there are only two ranks based on their number of occurrences.  

It seems that **case2** is more resealable, I will implement **case2** as part of our scenarios on this project.  
My solution for this case is to create a set() for storing the number of occurrences on the shortlist of required ranks, then generate the result based on the length of this set.  

---
## Usage
To test the application, change current directory to python_word_counter folder and run: 

```python
python word-counter.py input.txt
```  
In output.txt, the result would be:

```python
Top 10 Words: 
naomi 32 
luck 24 
tension 18 
two 15 
six 14 
alice 14 
jack 13 
one 11 
three 9 
four 9 
eight 8 
adfe 7 
Total Words: 194
```  


## Test
Test cases are mainly focusing on remove_puncuations(),merge_sort(), and outputs generated by the classes of InputFile and GetOutput.  
In production stage, it's better to use Mock in unittest for reading and writting file since it avoids modifying stuffs directly.  
However, it's kind of wordy for this project if I use Mock. hence I will create test files in txt_for_test folder and create the tests directly.  
For some cases related to loading directories, please use os module to handle the path cases in different environemnts.  
  
To check tests, change current directory to python_word_counter folder and run:    

```python
python -m unittest test
``` 
---
##  Contributors
- Jarick Chen <jarick@live.ca>
---
## License & Copyright
&copy; Jarick Chen

