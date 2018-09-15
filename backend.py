import numpy

test1 = "Multiply 3 and 4"
test2 = "Set x to 3"
test3 = "Output quote hello world endquote"


"""
1. Create list of words from input --> DONE
2. Separate strings from (based on endquote) --> DONE
3. Change numbers to floats and ints, and remove excess words --> DONE
3. Create "phrases" --> DONE
    > [keyword, [arguments_list]]
    > test1  --> ["multiply", [3,4]] 
4. map phrases to output
    > ["multiply", [3,4]] --> "3 * 4"
5. write to new line in .py file
"""

#Placeholder keywords, to be filled in by tony
keywords = {"output","print","add","multiply","set","to"} 
variables = {"x"}
valuable_strings = set()

def word_list(input_string):
    #makes all the words in the input string lowercase
    lowered_string = input_string.lower()
    # splits up the lowercase sentence into individual words
    return lowered_string.split(" ")

test = test3

print ("---------")
print("Original String: ", test)
test_words = word_list(test)

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
            valuable_strings.add(new_string[:-1]) #adds real strings to the keywords section
        else:
            final_words.append(words[i])
            i += 1
    return final_words
separated_words = separate_string(test_words)
print ("---------")
print ("Separated Words: ", separated_words)

"""
this function casts all numbers, like "three" and "four hundred point 5" to floats. 
It also removes all non-string and non-command words (such as "and")
"""
def remove_excess(words):
    final_items = []
    for word in words:
        if word in keywords:
            final_items.append(word)
        elif word in variables:
            final_items.append(word)
        elif word in valuable_strings:
            final_items.append(word)
        else:
            try:
                float(word)
                final_items.append(float(word))
            except ValueError:
                pass
    return final_items

final_items = remove_excess(separated_words)
print ("---------")
print("Final Items: ", final_items)