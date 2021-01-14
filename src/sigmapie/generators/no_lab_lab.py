from random import choice

def no_lab_lab(sigma = ("a", "n", "y", "u"), length = 4):
    """
    This function generates either a word grammatical with respect to a rule
    of no_lab_lab.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the no_lab_lab constraint. 
    """

    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    string = "".join([choice(sigma) for i in range(length)])
    
    n = string.count("y") + string.count("u")
    if n>1:
        return None
    else:
        return (string)  

def generate_nll(n = 10, sigma = ("a", "n", "y", "u"), length = 4):
    """
    Generates a set of strings or pairs that satisfy the rule of
    the no_lab_lab.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see no_lab_lab.
    
    Outputs:
    * list: a list of strings representing the application of no_lab_lab.
    """
    return [no_lab_lab(sigma, length) for i in range(n)]