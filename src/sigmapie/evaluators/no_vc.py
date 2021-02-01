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
    irrelevant = 0
    for w in data:
        if 'a' not in w:
            irrelevant += 1
        elif 'a' in w:
            temp_word = w[w.index('a'):]
            if 't' not in temp_word:
                correct += 1
    sum = len(data) - irrelevant 
    ratio = (correct / sum)
    print(f"Percentage of nvc well-formed words: {int(ratio * 100)}%.")