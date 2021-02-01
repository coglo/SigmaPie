from random import choice
'''
ə → o / w _ #, or _ u 
'''

def schwa_roundness(length = 4):
    """
    This function generates either a word grammatical with respect to a rule
    of schwa_roundness harmony.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the schwa_roundness harmony. 
    """
    sigma = ["n", "ə", "u"]

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"
    word = word.replace("uə<", "uo<").replace("əu", "ou")
    return word[1:length+1]


def schwa_roundness_io(length = 4):
    """
    This generator generates the fake input and output pairs of Mandarin syllable.
    
    Arguments:
    * n (int): a number of strings that need to be generated;
    ... for the rest of the arguments, see schwa_roundness.
    
    Outputs:
    *fake Mandarin pairs.
    """
    sigma = ["n", "ə", "u"]

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"

    word = word.replace("uə<", "uo<").replace("əu", "ou")
    return ((string, word[1:length+1])) 

def generate_sro(n = 10, length = 4):
    """
    Generates a set of strings that satisfy the rule of
    the schwa_roundness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see schwa_roundness.
    
    Outputs:
    * list: a list of strings representing the application of schwa_roundness harmony.
    """
    return [schwa_roundness(length) for i in range(n)]

def generate_sro_io(n = 10, sigma = ["n", "ə", "u"], length = 4):
    """
    Generates a set of pairs that satisfy the rule of
    the schwa_roundness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see schwa_roundness.
    
    Outputs:
    * list: a list of input & output pairs representing the application of schwa_roundness harmony.
    """
    return [schwa_roundness_io(length) for i in range(n)]
'''
data = generate_sro(n = 100, length = 4)
print("DATA", data)
for word in data:
    word = '>' + word + '<'
    if "əu" in word or "uə<" in word:
        print("BAD", word)
print("DONE")
'''
def schwa_roundness_bad(length = 4):
    sigma = ["n", "ə", "u"]

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length-2)]) + choice(["uə", "əu"])
    return string

def generate_sro_bad(n = 10, length = 4):
    return [schwa_roundness_bad(length=length) for i in range(n)]
