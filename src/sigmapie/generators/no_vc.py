from random import choice

def no_vc(length = 10):
    """
    This function generates either a word grammatical with respect to a rule
    of no_vc.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * length (int): a length of the intended words;
                    
    Outputs:
    * str: a string representing the application of the no_vc constraint. 
    """
    sigma = ["a", "n", "t"]
    if length < 1:
        raise ValueError("The string has a very weird length.")

    word = []
    for i in range(length):
        selection = choice(["a", "n"])

        #if selection is "a":
            #try:
                #sigma.remove('t')
            #except ValueError:
                #pass
        word.append(selection)
    string = "t" + "".join(word)
    return(string)

def generate_nvc(n = 10, length = 10):
    """
    Generates a set of strings or pairs that satisfy the rule of
    the no_vc.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see no_vc.
    
    Outputs:
    * list: a list of strings representing the application of no_vc.
    """
    return [no_vc(length) for i in range(n)]

def no_vc_bad(length = 10):
    sigma = ["a", "n", "t"]

    if length < 1:
        raise ValueError("The string has a very weird length.")

    word = []
    for i in range(length-1):
        selection = choice(["a", "n"])
        word.append(selection)
    string = "".join(word) + "t"
    return(string)

def generate_nvc_bad(n = 10, length = 10):
    return [no_vc_bad(length=length) for i in range(n)]