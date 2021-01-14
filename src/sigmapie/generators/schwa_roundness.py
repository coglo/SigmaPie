from random import choice
'''
ə → o / w _ #, or _ u 
'''

def schwa_roundness(sigma = ["a", "n", "ə", "u"], length = 4):
    """
    This function generates either a word grammatical with respect to a rule
    of schwa_roundness harmony.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the schwa_roundness harmony. 
    """

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"
    if "uə<" in word:
        word.replace("uə<", "uo<")
        return (word[1:5])
    if "əu" in word:
        word.replace("əu", "ou")
        return (word[1:5])
    else:
        return (string)  

def schwa_roundness_io(sigma = ["a", "n", "ə", "u"], length = 4):
    """
    This generator generates the fake input and output pairs of Mandarin syllable.
    
    Arguments:
    * n (int): a number of strings that need to be generated;
    ... for the rest of the arguments, see schwa_roundness.
    
    Outputs:
    *fake Mandarin pairs.
    """
    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"
    
    if "uə<" in word:
        word.replace("uə<", "uo<")
        return ((string, word[1:5]))
    if "əu" in word:
        word.replace("əu", "ou")
        return ((string, word[1:5]))
    else:
        return ((string, string))  

def generate_sro(n = 10, sigma = ["a", "n", "ə", "u"], length = 4):
    """
    Generates a set of strings that satisfy the rule of
    the schwa_roundness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see schwa_roundness.
    
    Outputs:
    * list: a list of strings representing the application of schwa_roundness harmony.
    """
    return [schwa_roundness(sigma, length) for i in range(n)]

def generate_sro_io(n = 10, sigma = ["a", "n", "ə", "u"], length = 4):
    """
    Generates a set of pairs that satisfy the rule of
    the schwa_roundness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see schwa_roundness.
    
    Outputs:
    * list: a list of input & output pairs representing the application of schwa_roundness harmony.
    """
    return [schwa_roundness_io(sigma, length) for i in range(n)]
