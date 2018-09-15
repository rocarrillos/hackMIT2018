import numpy

test1 = "Multiply three and four"
test2 = "Set x to three"
test3 = "Output quote hello world endquote"


"""
1. Create list of words from input --> DONE
2. Separate strings from (based on endquote) --> DONE
3. Change numbers to floats and ints --> IN PROGRESS
3. Create "phrases" --> DONE
    > [keyword, [arguments_list]]
    > test1  --> ["multiply", [3,4]] 
4. map phrases to output
    > ["multiply", [3,4]] --> "3 * 4"
5. write to new line in .py file
"""

def word_list(input_string):
    #makes all the words in the input string lowercase
    lowered_string = input_string.lower()
    # splits up the lowercase sentence into individual words
    return lowered_string.split(" ")

test1_words = word_list(test3)

def separate_string(words):
    final_words = []
    i = 0
    while i<len(words):
        if words[i] == "quote": #this identifies the beginning of the quote
            new_string = "" #creates the actual string, without 'quote' and endquote'
            i += 1
            element = words[i]
            while element != "endquote":
                new_string += words[i]
                new_string += " "
                i += 1
                element = words[i]
            i += 1
            final_words.append(new_string[:-1])
        else:
            final_words.append(words[i])
            i += 1
    return final_words
print (separate_string(test1_words))

keywords = ["output","print","add","multiply"] #Placeholder keywords, to be filled in by tony

def replace_numbers(words):
    pass

