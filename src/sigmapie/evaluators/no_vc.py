import re

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
    word_ls = []
    for w in data:
        if 'a' in w and "t" in w:
            word_ls.append(w)
    for wd in set(word_ls):
        temp_word = wd[wd.index('a'):]
        if 't' not in temp_word:
            correct += 1
    ratio = (correct / len(set(word_ls)))
    print(f"Percentage of nvc well-formed words: {int(ratio * 100)}%.")
    

def has_cons(sequence):
    """
    Check if a consonate is found in a string.
    This is needed because some of the consonants have multiple characters.
    """
    cons_ls= {"p", "b", "m", "f", "t", "d", "l", "ts", "tsʰ", "s", "tʂ", "tʂʰ", "ʂ", "ʐ", "tɕ", "tɕʰ", "ɕ", "k", "g", "h"}
    for cons in cons_ls:
        if cons in sequence:
            return True
    return False

def is_correct(word):
    vowel_ls={"a", "e", "ɑ", "ə", "u", "y", "i", "o"}
    """Returns True if there are no consonates following the first vowel."""
    return not any([has_cons(sequence) for sequence in re.split('|'.join(vowel_ls), word)[1:]])

def evaluate_nvc_real_words(data):
    vowel_ls={"a", "e", "ɑ", "ə", "u", "y", "i", "o"}

    filtered_words = [word for word in data if vowel_ls.intersection(word) and has_cons(word)]

    number_correct = sum([True for word in filtered_words if is_correct(word)])

    ratio = (number_correct / len(filtered_words))
    print(f"Percentage of nvc well-formed words: {int(ratio * 100)}%.")

def evaluate_nvc_masked_words(data):
    vowel_ls={"a", "e", "ɑ", "ə", "u", "y", "i", "o"}

    filtered_words = [word for word in data if vowel_ls.intersection(word) and has_cons(word)]

    number_correct = sum([True for word in filtered_words if is_correct(word)])

    ratio = (number_correct / len(filtered_words))
    print(f"Percentage of nvc well-formed words: {int(ratio * 100)}%.")