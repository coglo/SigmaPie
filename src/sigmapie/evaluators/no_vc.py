def evaluate_nvc_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of no_vc.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    for w in data:
        if "t" in string and "a" in string:
            n = string.index("t")
            m = string.index("a")
            if n > m:
                correct += 0
        else:
            correct += 1
 
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")