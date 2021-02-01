
def well_formed(word, restrictions):
    """ Checks if one of the restrictions is contained in the word """
    for restriction in restrictions:
        if restriction in word:
            return False
    return True

def evaluate_vfr_words(data):
    """
    Evaluates the provided words with respect to the rule 
    of vowel_frontness harmony.
    
    Arguments:
    * data (list[str]): a list of strings tht need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    restrictions = ["iə<", "yə<", "iən", "yən", "au", "aŋ"]

    # Mark start and end of words.
    data = ['>' + word + '<' for word in data]

    # Find the ratio of words with no restrictions to total words.
    ratio = sum([well_formed(word, restrictions) for word in data])/len(data)
    return ratio * 100
    #print(f"Percentage of vfr well-formed words: {int(ratio * 100)}%.")


def evaluate_vfr_io(data):
    """
    Evaluates the provided pairs with respect to the rule 
    of vowel_frontness harmony.
    
    Arguments:
    * data (list[str]): a list of strings/tuples that need to be evaluated;
                       
    Results:
    * Prints the report that shows if the data follows the rule.
    """
    restrictions = ["iə<", "yə<", "iən", "yən", "au", "aŋ"]
    SF_ls = []
    for w in data:
        UR, SF = w
        assert len(UR) == len(SF)
        # Mark start and end of words.
        SF_word = ">" + SF + "<"
        SF_ls.append(SF_word)

    # Find the ratio of words with no restrictions to total words.
    ratio = sum([well_formed(SF_word, restrictions) for SF_word in SF_ls])/len(data)
    return ratio * 100
    #print(f"Percentage of vfr_io well-formed words: {int(ratio * 100)}%.")
