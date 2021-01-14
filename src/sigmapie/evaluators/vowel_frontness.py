def evaluate_vfr_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of vowel_frontness harmony.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    disallowed = ["iə<", "yə<", "iən", "yən", "au", "aŋ"]
    correct = 0
    for w in data:
        word = ">" + w + "<"
        for d in disallowed:
            if d in word:
                correct += 0
        else:
            correct += 1
 
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")


def evaluate_vfr_io(data):
    """
    Evaluates the provided pairs with respect to the rule 
    of vowel_frontness harmony.
    
    Arguments:
    * data (list[str]): a list of strings/tuples that need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    disallowed = ["iə<", "yə<", "iən", "yən", "au", "aŋ"]
    correct = 0  
    for w in data:
        UR, SF = w
        assert len(UR) == len(SF)
    
        SF1 = ">" + SF + "<"
        
        for d in disallowed:
            if d not in SF1:
                break
        correct += 1
        
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")