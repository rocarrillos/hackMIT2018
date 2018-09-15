import numpy

test1 = "Multiply three and four"
test2 = "Set x to three"
test3 = "Output quote hello world end quote"


"""
1. Create list of words from input --> DONE
2. Separate strings from (based on endquote)
3. Create "phrases"
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

test1_words = word_list(test1)
print (test1_words)    


    
