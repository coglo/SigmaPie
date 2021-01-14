def evaluate_nhh_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of no_high_high.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    for w in data:
        n = w.count("y") + w.count("u")
        m = w.count("y") + w.count("i")
        if n>1:
            correct += 0
        elif m>1:
            correct += 0
        else:
            correct += 1
 
    ratio = (correct / len(data))
    print(f"Percentage of well-formed words: {int(ratio * 100)}%.")