from random import choice

def word_final_devoicing(sigma = ("a", "b", "p"), devoice = (("b"), ("p")),
                         length = 10, pairs = False):
    """
    This function generates either a word grammatical with respect to a rule
    of the word final devoicing, or a fake UG -> SF pair.
    
    Arguments: 
    * sigma (list[str]): a list of symbols that can be used in the words;
    * devoice (tuple[tuple, tuple]): the first tuple represents voiced
                                     obstruents, and the second one stands
                                     for their voiceless counterparts;
    * length (int): a length of the intended words;
    * pairs (bool): if True, (UG, SF) pairs will be returned, if False, only
                    the surface forms.
                    
    Outputs:
    * str/tuple: a string or a tuple of strings (depending on the parameter 
                 `pairs`) representing the application of the word-final 
                 devoicing.
    """
    if length < 1:
        raise ValueError("The string has a very weird length.")
        
    before, after = devoice
    string = "".join([choice(sigma) for i in range(length)])
    
    if string[-1] not in before:
        return (string, string) if pairs else string
    
    devoiced = string[:-1] + after[before.index(string[-1])]
    return (string, devoiced) if pairs else devoiced

def generate_wfd(n = 10, sigma = ("a", "b", "p"), devoice = (("b"), ("p")),
                 length = 10, pairs = False):
    """
    Generates a set of strings or pairs that satisfy the rule of
    the word-final devoicing.
    
    Arguments:
    * n (int): the number of strings that need to be generated;
    ... for the rest of the arguments see word_final_devoicing.
    
    Outputs:
    * list: a list of strings or tuples (depending on the parameter `pairs`)
            representing the application of the word-final devoicing.
    """
    return [word_final_devoicing(sigma, devoice, length, pairs) for i in range(n)]