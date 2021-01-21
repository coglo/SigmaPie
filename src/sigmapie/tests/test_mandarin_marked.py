from sigmapie.generators.no_lab_lab import generate_nll, no_lab_lab
from sigmapie.evaluators.no_lab_lab import evaluate_nll_words
from sigmapie.generators.no_cor_cor import generate_ncc, no_cor_cor
from sigmapie.evaluators.no_cor_cor import evaluate_ncc_words
from sigmapie.generators.no_high_high import generate_nhh, no_high_high
from sigmapie.evaluators.no_high_high import evaluate_nhh_words
from sigmapie.generators.no_vc import generate_nvc, no_vc
from sigmapie.evaluators.no_vc import evaluate_nvc_words  
from sigmapie.generators.schwa_roundness import generate_sro, generate_sro_io, schwa_roundness, schwa_roundness_io
from sigmapie.evaluators.schwa_roundness import evaluate_sro_words, evaluate_sro_io
from sigmapie.generators.vowel_frontness import generate_vfr, generate_vfr_io, vowel_frontness, vowel_frontness_io
from sigmapie.evaluators.vowel_frontness import evaluate_vfr_words, evaluate_vfr_io
from sigmapie.sp_class import SP
from sigmapie.sl_class import SL
from sigmapie.tsl_class import TSL
from sigmapie.mtsl_class import MTSL
import string
import random
import itertools
import collections
from collections import defaultdict
import csv

def get_masked_mandarin_words(keep_list=["a", "e", "n", "ɑ","ŋ","n", "ə", "u", "y", "i", "t"]):
    with open('C:/Users/19061/git/phomo/phomo/mandarin_words.csv', newline='') as f:
        reader = csv.reader(f)
        word_ls = [word[0] for word in list(reader)]
    new_word_list = []
    for word in word_ls:
        for i in word:
            if i not in keep_list:
                word = word.replace(i, "x")
        new_word_list.append(word)
    return new_word_list

def get_masked_mandarin_nonwords(keep_list=["a", "e", "n", "ɑ", "ŋ", "n", "ə", "u", "y", "i", "t"]):
    with open('C:/Users/19061/git/phomo/phomo/mandarin_nonwords.csv', newline='') as f:
        reader = csv.reader(f)
        word_ls = [word[0] for word in list(reader)]
    new_word_list = []
    for word in word_ls:
        for i in word:
            if i not in keep_list:
                word = word.replace(i, "x")
        new_word_list.append(word)
    return new_word_list

def evaluate_models(evaluator, data, tsl=True):
    
    '''
    sp_h = SP(polar="n")
    sl_h = SL(polar="n")
    tsl_h = TSL(polar="n")
    mtsl_h = MTSL(polar="n")
    '''
    sp_h = SP()
    sl_h = SL()
    tsl_h = TSL()
    mtsl_h = MTSL()

    sp_h.data = data
    sl_h.data = data
    tsl_h.data = data
    mtsl_h.data = data
    
    sp_h.extract_alphabet()
    sl_h.extract_alphabet()
    tsl_h.extract_alphabet()
    mtsl_h.extract_alphabet()
    
    sp_h.learn()
    sl_h.learn()
    tsl_h.learn()
    mtsl_h.learn()

    evaluator(data)
    evaluator(sl_h.generate_sample(n=1000, repeat=True))
    evaluator(sp_h.generate_sample(n=1000, repeat=True))
    if tsl:
        evaluator(tsl_h.generate_sample(n=1000, repeat=True))
    evaluator(mtsl_h.generate_sample(n=1000, repeat=True))
    
    print("SL k:", sl_h.k)
    print("SL sample:", sl_h.generate_sample(20, repeat=False), "\n")
    print("SP sample:", sp_h.generate_sample(20, repeat=False), "\n")
    if tsl:
        print("TSL tier:", tsl_h.tier)
        print("TSL sample:", tsl_h.generate_sample(20, repeat=False), "\n")
    print("MTSL tiers:", mtsl_h.tier)
    print("MTSL sample:", mtsl_h.generate_sample(20, repeat=False))
    print("SL alphabet:", sl_h.alphabet)
    print("SP alphabet:", sp_h.alphabet)
    if tsl:
        print("TSL alphabet:", tsl_h.alphabet)
    print("MTSL alphabet:", mtsl_h.alphabet)

    print("SL grammar:", sl_h.grammar)
    print("SP grammar:", sp_h.grammar)
    print("TSL grammar:", tsl_h.grammar)
    print("MTSL grammar:", mtsl_h.grammar)

    print("SL polarity:", sl_h.check_polarity())
    print("SP polarity:", sp_h.check_polarity())
    if tsl:
        print("TSL polarity:", tsl_h.check_polarity())
    print("MTSL polarity:", mtsl_h.check_polarity())

def test_no_lab_lab():
    data = get_masked_mandarin_words(keep_list=["n", "u", "y"])
    datan = get_masked_mandarin_nonwords(keep_list=["n", "u", "y"])
    evaluate_models(evaluate_nll_words, data)
    #evaluate_nll_words(datan)

def test_no_cor_cor():
    data = get_masked_mandarin_words(keep_list=["n", "i", "y"])
    evaluate_models(evaluate_ncc_words, data)

def test_no_high_high():
    data = get_masked_mandarin_words(keep_list=["i", "n", "u", "y"])
    evaluate_models(evaluate_nhh_words, data)

def test_no_vc():
    data = get_masked_mandarin_words(keep_list=["n", "t", "a"])
    evaluate_models(evaluate_nvc_words, data)

def test_schwa_roundness():
    data = get_masked_mandarin_words(keep_list=["n", "ə", "u", "o"])
    evaluate_models(evaluate_sro_words, data, tsl=False)

def test_vowel_frontness():
    data = get_masked_mandarin_words(keep_list=["a", "ə", "e", "ɑ", "i", "y", "n", "u", "ŋ"])
    evaluate_models(evaluate_vfr_words, data)
    