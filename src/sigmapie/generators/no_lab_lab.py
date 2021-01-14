from random import choice

def no_lab_lab(sigma = ["a", "n", "y", "u"], length = 4):
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

    word = []
    for i in range(length):
        selection = choice(sigma)
        if selection in ['y', 'u']:
            sigma.remove('y')
            sigma.remove('u')
        word.append(selection)
    string = "".join(word)
    return(string)

def generate_nll(n = 10, sigma = ["a", "n", "y", "u"], length = 4):
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