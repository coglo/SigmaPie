def evaluate_wfd_words(data, voiced = ("b")):
    """
    Evaluates the provided words with respect to the rule 
    of the word-final devoicing.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
    * voiced (tuple[char]): a list of voiced characters, i.e. those
                            that cannot be word-final.
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    for w in data:
        
        if not len(w):
            correct += 1
            continue
            
        correct = (correct + 1) if w[-1] not in voiced else correct
        
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")

def evaluate_wfd_pairs(data, devoice = (("b"), ("p"))):
    """
    Evaluates the provided pairs with respect to the rule 
    of the word-final devoicing.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
    * voiced (tuple[char]): a list of voiced characters, i.e. those
                            that cannot be word-final.
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    before, after = devoice
    
    for w in data:
        
        UR, SF = w
        assert len(UR) == len(SF)
        
        if not len(UR):
            correct += 1
            continue
        
        if UR[-1] not in before:
            correct = (correct + 1) if UR == SF else correct
            continue
        
        SF_bar = UR[:-1] + after[before.index(UR[-1])]
        correct = (correct + 1) if SF == SF_bar else correct
        
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")