def evaluate_sro_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of schwa_roundness harmony.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    for w in data:
        word = ">" + w + "<"
        if "uə<" in word or "əu" in word:
            correct += 0
        else:
            correct += 1
 
    ratio = (correct / len(data))
    print(f"Percentage of sro well-formed words: {int(ratio * 100)}%.")


def evaluate_sro_io(data):
    """
    Evaluates the provided pairs with respect to the rule 
    of schwa_roundness harmony.
    
    Arguments:
    * data (list[str]): a list of strings/tuples that need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0  
    for w in data:
        UR, SF = w
        assert len(UR) == len(SF)
    
        SF1 = ">" + SF + "<"

        if "uə<" not in SF1 and "əu" not in SF1:
            correct += 1
        else:
            correct += 0
        
    ratio = (correct / len(data))
    print(f"Percentage of sro_io well-formed words: {int(ratio * 100)}%.")