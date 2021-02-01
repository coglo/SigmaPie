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

        if 'a' in w:
            temp_word = w[w.index('a'):]
            if 't' not in temp_word:
                correct += 1
        else:
            correct += 1
 
    ratio = (correct / len(data))
    return ratio * 100
    #print(f"Percentage of nvc well-formed words: {int(ratio * 100)}%.")