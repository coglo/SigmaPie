from random import choice

def no_cor_cor(length = 10):
    """
    This function generates either a word grammatical with respect to a rule
    of no_cor_cor.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the no_cor_cor constraint. 
    """
    sigma = ["n", "y", "i"]

    if length < 1:
        raise ValueError("The string has a very weird length.")

    word = []
    for i in range(length):
        selection = choice(sigma)
        if selection in ['y', 'i']:
            sigma.remove('y')
            sigma.remove('i')
        word.append(selection)
    string = "".join(word)
    return(string)

def generate_ncc(n = 10, length = 10):
    """
    Generates a set of strings or pairs that satisfy the rule of
    the no_cor_cor.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see no_cor_cor.
    
    Outputs:
    * list: a list of strings representing the application of no_cor_cor.
    """
    return [no_cor_cor(length) for i in range(n)]

def no_cor_cor_bad(length = 10):
    sigma = ["n", "y", "i"]

    if length < 1:
        raise ValueError("The string has a very weird length.")

    word = []
    for i in range(length):
        selection = choice(sigma)
        word.append(selection)

    w = "".join(word)
    string = w.replace(choice(list(w)), choice(["i", "y"])) + choice(["i", "y"])
    return(string)


def generate_ncc_bad(n = 10, length = 10):
    return [no_cor_cor_bad(length=length) for i in range(n)]