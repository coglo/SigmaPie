def evaluate_nll_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of no_lab_lab.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    correct = 0
    irrelevant = 0
    for w in data:
        if "y" not in w and "u" not in w:
            irrelevant += 1
        n = w.count("y") + w.count("u")
        if n<=1 and n >0:
            correct += 1
    sum = len(data) - irrelevant
    ratio = (correct / sum)
    return ratio * 100
    #print(f"Percentage of nll well-formed words: {int(ratio * 100)}%.")


'''
def evaluate_nll_words_bad(data):
    incorrect = 0
    for w in data:
        n = w.count("y") + w.count("u")
        if n>1:
            incorrect += 1
 
    ratio = (incorrect / len(data))
    print(f"Percentage of nll well-formed words: {int(ratio * 100)}%.")

def evaluate_nll_words_all(data_good, data_bad):
    correct = 0
    for w in data_good:
        n = w.count("y") + w.count("u")
        if n<=1:
            correct += 1

    incorrect = 0
    for w in data_bad:
        n = w.count("y") + w.count("u")
        if n>1:
            incorrect += 1
    
    data = data_good + data_bad
    accuracy = correct + incorrect

    ratio = (accuracy / len(data))
    print(f"Accuracy of nll evaluator: {int(ratio * 100)}%.")
    '''





 