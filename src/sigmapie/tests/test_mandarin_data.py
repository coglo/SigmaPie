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

def get_mandarin_words():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_words.csv', newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

def get_mandarin_nonwords():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_nonwords.csv', newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

def test_no_lab_lab():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_nll_words(data)
    evaluate_nll_words(datan)

def test_no_cor_cor():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_ncc_words(data)
    evaluate_ncc_words(datan)

def test_no_high_high():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_nhh_words(data)
    evaluate_nhh_words(datan)

def test_no_vc():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_nvc_words(data)
    evaluate_nvc_words(datan)

def test_schwa_roundness():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_sro_words(data)
    evaluate_sro_words(datan)

def test_vowel_frontness():

    data = get_mandarin_words()
    datan = get_mandarin_nonwords()

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

    evaluate_vfr_words(data)
    evaluate_vfr_words(datan)
 