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
    irrelevant = 0
    for w in data:
        if "y" not in w and "i" not in w:
            irrelevant += 1
        n = w.count("y") + w.count("i")
        if n<=1 and n >0:
            correct += 1
    sum = len(data) - irrelevant
    ratio = (correct / sum)
    print(f"Percentage of ncc well-formed words: {int(ratio * 100)}%.")
    