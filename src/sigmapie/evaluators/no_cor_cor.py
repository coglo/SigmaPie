def evaluate_ncc_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of no_cor_cor.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    for w in data:
        n = w.count("y") + w.count("i")
        if n<=1:
            correct += 1
 
    ratio = (correct / len(data))
    return ratio * 100
    #print(f"Percentage of ncc well-formed words: {int(ratio * 100)}%.")