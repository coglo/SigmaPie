from random import choice
'''
ə → e / j, ɥ _#
a → e / j, ɥ _ n
a → ɑ / _ u, ŋ

'''

def vowel_frontness(length = 10):
    """
    This function generates either a word grammatical with respect to a rule
    of vowel_frontness harmony.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the vowel_frontness harmony. 
    """
    sigma = ["a", "ə", "i", "y", "n", "u", "ŋ"]

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"
    word = word.replace("iə<", "ie<").replace("yə<", "ye<").replace("iən", "ien").replace("yən", "yen").replace("au", "ɑu").replace("aŋ", "ɑŋ")
    return word[1:length+1] 

def vowel_frontness_io(length = 10):
    """
    This generator generates the fake input and output pairs of Mandarin syllable.
    
    Arguments:
    * n (int): a number of strings that need to be generated;
    ... for the rest of the arguments, see vowel_frontness.
    
    Outputs:
    *fake Mandarin pairs.
    """
    sigma = ["a", "ə", "i", "y", "n", "u", "ŋ"]
    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    word = ">" + string + "<"
    '''
    if "iə<" in word:
        word = word.replace("iə<", "ie<")
        return (string, word[1:length+1])
    if "yə<" in word:
        word = word.replace("yə<", "ye<")
        return (string, word[1:length+1])
    if "iən" in word:
        word = word.replace("iən", "ien")
        return (string, word[1:length+1])
    if "yən" in word:
        word = word.replace("yən", "yen")
        return (string, word[1:length+1]) 
    if "au" in word:
        word = word.replace("au", "ɑu")
        return (string, word[1:length+1])
    if "aŋ" in word:
        word = word.replace("aŋ", "ɑŋ")
        return (string, word[1:length+1])
    else:
        return ((string, string))
    '''  
    word = word.replace("iə<", "ie<").replace("yə<", "ye<").replace("iən", "ien").replace("yən", "yen").replace("au", "ɑu").replace("aŋ", "ɑŋ")
    return ((string, word[1:length+1])) 

def generate_vfr(n = 10, length = 10):
    """
    Generates a set of strings that satisfy the rule of
    the vowel_frontness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see vowel_frontness.
    
    Outputs:
    * list: a list of strings representing the application of vowel_frontness harmony.
    """
    return [vowel_frontness(length) for i in range(n)]

def generate_vfr_io(n = 10, length = 10):
    """
    Generates a set of pairs that satisfy the rule of
    the vowel_frontness harmony.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see vowel_frontness.
    
    Outputs:
    * list: a list of input & output pairs representing the application of vowel_frontness harmony.
    """
    return [vowel_frontness_io(length) for i in range(n)]


def vowel_frontness_bad(length = 10):
    sigma = ["a", "ə", "i", "y", "n", "u", "ŋ"]

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length-2)]) + choice(["iə", "yə", "iən", "yən", "au", "aŋ"])
    return string

def generate_vfr_bad(n = 10, length = 10):
    return [vowel_frontness_bad(length=length) for i in range(n)]