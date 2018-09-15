# input ["multiply", "three", "and", "four"]



def make_phrase(words):
    # end condition: hit the end of the list
    if not words: 
        return []

    build = []

    for i, word in enumerate(words):
        # if you hit a key word, make a new list in format
        # ["keyword", arguments....]
        if word in keywords:
           build.append([word]+ make_phrase(words[i+1:]))
           break

        # if it is not a keyword, return the 
        else:
            build.append(word)  
    
    return build
            

class Operator:

    def __init__(self, value):
        self.value = str(value)

    
    def evaluate(self, args):

        result = "" # output

        for i, word in enumerate(args): 
            result += str(word) 

            # if not at the last argument, add the operator in 
            # between this argument and the next 
            if i < len(args)-1:
                result += " " + self.value + " "

        return result

def evaluate(argument):

    # all lists should start with a keyword at the first index
    # and arguments after that 
    if isinstance(argument, list):
        key, args = argument[0], argument[1:]
        args = evaluate()
        return keywords[key].evaluate(args)

    else:   
        return argument

mult = Operator("*")
mult_words = ["product", "multiply"]

add = Operator("+")
add_words = ["add", "sum"]

subtract = Operator("-")
subtract_words = ["subtract"]

set_var = Operator("=")
set_var_words = ["set"]

pairs = [(mult, mult_words), (add, add_words), (subtract, subtract_words), (set_var, set_var_words)]


keywords = dict()

for func, words in pairs:
    keywords.update({key : func for key in words})


list_ = ["set","x", "multiply", 4, "add", 5,3] # "multiply", 3, 4]
phrase = make_phrase(list_)
print(phrase)






    
"""
words = ["set",  "x", "multiply", 3, 4]
words0 = ["output", "hello world"]
words1 =  ["multiply", "three", "and", "four"]
print(make_phrase(words))
"""
