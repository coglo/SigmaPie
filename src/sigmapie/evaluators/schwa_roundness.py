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
    word_ls = []
    for w in data:
        word = ">" + w + "<"
        if "əu" in word or "uo<" in word or "ou" in word or "uə<" in word:
            word_ls.append(word)
    for wd in set(word_ls):
        if "uə<" not in wd and "əu" not in wd: 
            correct += 1

    #sum = len(data) - irrelevant
    ratio = (correct / len(set(word_ls)))
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
        
    ratio = (correct / len(data))
    print(f"Percentage of sro_io well-formed words: {int(ratio * 100)}%.")