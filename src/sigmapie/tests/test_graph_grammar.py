import networkx as nx
from networkx.drawing.nx_agraph import write_dot
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
from sigmapie.GraphGrammar_class import GraphGrammar
import pytest
from random import choice
import string
import random
import itertools
import collections
from collections import defaultdict
import csv

def evaluate_graphmodels(evaluator, data):
    graph_model = GraphGrammar(data)
    evaluator(graph_model.generate_sample(1000))
    graph_model.write_dot()
    evaluator(data)
    print("alphabet:", graph_model.alphabet)
    print("restricted pairs:", graph_model.restricted_pairs)
    print("Graphmodel sample:", graph_model.generate_sample(10), "\n")

def test_no_lab_lab_generated():
    evaluate_graphmodels(evaluate_nll_words, generate_nll(n=1000))

def test_no_cor_cor_generated():
    evaluate_graphmodels(evaluate_ncc_words, generate_ncc(n=1000))

def test_no_high_high_generated():
    evaluate_graphmodels(evaluate_nhh_words, generate_nhh(n=1000))

def test_no_vc_generated():
    evaluate_graphmodels(evaluate_nvc_words, generate_nvc(n=1000))

def test_schwa_roundness_generated():
    evaluate_graphmodels(evaluate_sro_words, generate_sro(n=1000))

def test_vowel_frontness_generated():
    evaluate_graphmodels(evaluate_vfr_words, generate_vfr(n=1000))


def get_mandarin_words():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_words.csv', encoding="utf-8-sig", newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

def get_mandarin_nonwords():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_nonwords.csv', encoding="utf-8-sig", newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

def test_no_lab_lab():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_nll_words, real_data)

def test_no_cor_cor():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_ncc_words, real_data)

def test_no_high_high():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_nhh_words, real_data)

def test_no_vc():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_nvc_words, real_data)

def test_schwa_roundness():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_sro_words, real_data)

def test_vowel_frontness():
    real_data = get_mandarin_words()
    evaluate_graphmodels(evaluate_vfr_words, real_data)


def get_masked_mandarin_words(keep_list=["a", "e", "n", "ɑ","ŋ","n", "ə", "u", "y", "i", "t"]):
    with open('C:/Users/19061/git/phomo/phomo/mandarin_words.csv', encoding="utf-8-sig", newline='') as f:
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
    with open('C:/Users/19061/git/phomo/phomo/mandarin_nonwords.csv', encoding="utf-8-sig", newline='') as f:
        reader = csv.reader(f)
        word_ls = [word[0] for word in list(reader)]
    new_word_list = []
    for word in word_ls:
        for i in word:
            if i not in keep_list:
                word = word.replace(i, "x")
        new_word_list.append(word)
    return new_word_list

def test_no_lab_lab_masked():
    mask_data = get_masked_mandarin_words(keep_list=["n", "u", "y"])
    evaluate_graphmodels(evaluate_nll_words, mask_data)
    #evaluate_nll_words(datan)

def test_no_cor_cor_masked():
    mask_data = get_masked_mandarin_words(keep_list=["n", "i", "y"])
    evaluate_graphmodels(evaluate_ncc_words, mask_data)

def test_no_high_high_masked():
    mask_data = get_masked_mandarin_words(keep_list=["i", "n", "u", "y"])
    evaluate_graphmodels(evaluate_nhh_words, mask_data)

def test_no_vc_masked():
    mask_data = get_masked_mandarin_words(keep_list=["n", "t", "a"])
    evaluate_graphmodels(evaluate_nvc_words, mask_data)

def test_schwa_roundness_masked():
    mask_data = get_masked_mandarin_words(keep_list=["n", "ə", "u", "o"])
    evaluate_graphmodels(evaluate_sro_words, mask_data)

def test_vowel_frontness_masked():
    mask_data = get_masked_mandarin_words(keep_list=["a", "ə", "e", "ɑ", "i", "y", "n", "u", "ŋ"])
    evaluate_graphmodels(evaluate_vfr_words, mask_data)