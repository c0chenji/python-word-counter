
from helper.help_functions import *

class InputFile:
    def __init__(self, filename, total_words=0):
        self.filename = filename
        self.total_words = total_words
        self.occurence_set = set()

    def count_and_save(self):
        counter = {}
        try:
            with open(self.filename, encoding="utf8") as f:
                for line in f.readlines():
                    # Trim every line(remove spaces on the left or right).
                    # Assume words are separated by spaces or punctuations, and split them into a list of words.
                    new_line = remove_punctuations(line).strip().lower()
                    target_list = new_line.split(" ")
                    # Count occurence of word and save/update records into dictionary.
                    # And also count the number of word at the same time.
                    for word in target_list:
                        # Check if string is letters or words
                        # Assume d1 12 G18 are not words
                        # if word !="":
                        if word.isalpha():
                            self.total_words += 1
                            w = word.strip()
                            counter[w] = 1 if w not in counter else counter[w]+1
                self.occurence_set ={v for v in counter.values()}
                return counter
        # # Normally we handle file not found error
        except FileNotFoundError as e:
            print(e)
        # Other errors
        except Exception as e:
            print(e)


class GetOutput:
    def __init__(self, filename):
        self.filename = filename

    def sorted_and_save(self):
        try:
            target = InputFile(self.filename)
            # total_words = target.total
            # # convert dictionary into list of tuples
            # # e.g {"hi":1,"hello":2} would be converted to [("hi",1),("hello",2)]
            # result = list(target.count_and_save().items())
            # # Update the target list in desending order with merge_sort

            self.saveOutput(target)
        except Exception as e:
            print(e)

    @staticmethod
    def saveOutput(target):
        result = list(target.count_and_save().items())
        # Value of total_words would only be update when count_and_save has been called
        total_words = target.total_words
        rank_available = len(target.occurence_set)
        # Sort the target list in desending order with merge_sort
        
        # merge_sort(result, 0, len(result) - 1)
        # or 
        heapSort(result)
        output_file = "output" + target.filename[-4:]
        try:
            with open(output_file, "w") as f:
                
                # Case 1: counter has more than 10 different words
                if rank_available >= 10:
                    f.writelines("Top {} Words:\n".format(10))
                    
                    # Another case: there may be multiple words has same number as the word on rank 10
                    add_qualified_words(f, result,10)
                    f.writelines("Total Words: {}".format(total_words))
                # Case 2: The num of different words in counter is less than 10
                elif rank_available > 0 and rank_available < 10:
                    f.writelines("Top {} Words:\n".format(rank_available))
                    for item in result:
                        f.writelines("{} {} \n".format(item[0], item[1]))
                        
                    f.writelines("Total Words: {}".format(total_words))
                # Case 3: empty file, no word
                else:
                    f.writelines("There is no word in this file.")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # inputResult = InputFile("input.txt")
    # result_dict = inputResult.count_and_save()
    output = GetOutput("input.txt").sorted_and_save()
   
