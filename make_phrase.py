# input ["multiply", "three", "and", "four"]

keywords = {"multiply", "add", "subtract"}

def make_phrase(words):

    for i, word in enumerate(words):
        word = words[i]
        if word in keywords:
            return [word, make_phrase(words[i:])]    
        else:
            return word
    pass    