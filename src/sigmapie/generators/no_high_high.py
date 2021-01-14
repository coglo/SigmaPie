from random import choice

def no_high_high(sigma = ["a", "n", "i", "y", "u"], length = 4):
    """
    This function generates either a word grammatical with respect to a rule
    of no_high_high.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the no_high_high constraint. 
    """
    if length < 1:
        raise ValueError("The string has a very weird length.")

    word = []
    for i in range(length):
        selection = choice(sigma)
        if selection == 'y':
            if 'y' in sigma: sigma.remove('y')
            if 'i' in sigma: sigma.remove('i')
            if 'u' in sigma: sigma.remove('u')
        elif selection == 'i':
            if 'y' in sigma: sigma.remove('y')
            if 'i' in sigma: sigma.remove('i')
        elif selection == 'u':
            if 'y' in sigma: sigma.remove('y')
            if 'u' in sigma: sigma.remove('u')
        word.append(selection)
    string = "".join(word)
    return(string)

def generate_nhh(n = 10, sigma = ["a", "n", "i", "y", "u"], length = 4):
    """
    Generates a set of strings or pairs that satisfy the rule of
    the no_high_high.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see no_high_high.
    
    Outputs:
    * list: a list of strings representing the application of no_high_high.
    """
    return [no_high_high(sigma, length) for i in range(n)]