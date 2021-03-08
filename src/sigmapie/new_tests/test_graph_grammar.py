import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from sigmapie.generators.no_lab_lab import generate_nll, no_lab_lab, generate_nll_bad, no_lab_lab_bad
from sigmapie.evaluators.no_lab_lab import evaluate_nll_words 
from sigmapie.generators.no_fro_fro import generate_nff, no_fro_fro, generate_nff_bad, no_fro_fro_bad
from sigmapie.evaluators.no_fro_fro import evaluate_nff_words
from sigmapie.generators.no_high_high import generate_nhh, no_high_high, generate_nhh_bad, no_high_high_bad
from sigmapie.evaluators.no_high_high import evaluate_nhh_words
from sigmapie.generators.no_vc import generate_nvc, no_vc, generate_nvc_bad, no_vc_bad
from sigmapie.evaluators.no_vc import evaluate_nvc_words, evaluate_nvc_real_words, evaluate_nvc_masked_words 
from sigmapie.generators.schwa_roundness import generate_sro, generate_sro_io, schwa_roundness, schwa_roundness_io, generate_sro_bad, schwa_roundness_bad
from sigmapie.evaluators.schwa_roundness import evaluate_sro_words, evaluate_sro_io
from sigmapie.generators.vowel_frontness import generate_vfr, generate_vfr_io, vowel_frontness, vowel_frontness_io, generate_vfr_bad, vowel_frontness_bad
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

def evaluate_graphmodels(evaluator, data, datan):
    graph_model = GraphGrammar(data)

    print("-------", evaluator.__name__, "------")

    '''
    print("graph model generated data", round(evaluator(graph_model.generate_sample(1000)), 3))
    print("generator genarated data", round(evaluator(data), 3))
    print("generator generated data", "graph_model.percent_grammatical", round(graph_model.percent_grammatical(data), 3), "\n")
    print("generator generated data_bad", "graph_model.percent_grammatical", round(graph_model.percent_grammatical(datan), 3), "\n")
    '''

    evaluator(data)
    evaluator(datan)

    evaluator(graph_model.generate_sample(1000))
    #print(graph_model.percent_grammatical(data))
    #print(datan[0:20], "\n")
    #print(graph_model.percent_grammatical(datan))

    print("alphabet:", graph_model.alphabet)
    print("restricted pairs:", graph_model.restricted_pairs)
    print("Graphmodel sample:", graph_model.generate_sample(10), "\n")
    print("edges and nodes:", graph_model.show_graph_edges(data), "\n")

def test_no_lab_lab_generated():
    evaluate_graphmodels(evaluate_nll_words, generate_nll(n=1000), generate_nll_bad(n=1000))

def test_no_fro_fro_generated():
    evaluate_graphmodels(evaluate_nff_words, generate_nff(n=1000), generate_nff_bad(n=1000))

def test_no_high_high_generated():
    evaluate_graphmodels(evaluate_nhh_words, generate_nhh(n=1000), generate_nhh_bad(n=1000))

def test_no_vc_generated():
    evaluate_graphmodels(evaluate_nvc_words, generate_nvc(n=1000), generate_nvc_bad(n=1000))

def test_schwa_roundness_generated():
    evaluate_graphmodels(evaluate_sro_words, generate_sro(n=1000), generate_sro_bad(n=1000))

def test_vowel_frontness_generated():
    evaluate_graphmodels(evaluate_vfr_words, generate_vfr(n=1000), generate_vfr_bad(n=1000))

def get_mandarin_words():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_words.csv', encoding="utf-8-sig", newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

def get_mandarin_nonwords():
    with open('C:/Users/19061/git/phomo/phomo/mandarin_nonwords.csv', encoding="utf-8-sig", newline='') as f:
        reader = csv.reader(f)
        return [word[0] for word in list(reader)]

cons_ls= ["p", "b", "m", "f", "t", "d", "l", "ts", "tsʰ", "s", "tʂ", "tʂʰ", "ʂ", "ʐ", "tɕ", "tɕʰ", "ɕ", "k", "g", "h"]

def test_no_lab_lab():
    real_data = get_mandarin_words()
    bad_data = [w.replace(choice(list(w)), choice(["u", "y"])) + choice(["u", "y"])  for w in real_data]
    evaluate_graphmodels(evaluate_nll_words, real_data, bad_data)

def test_no_fro_fro():
    real_data = get_mandarin_words()
    bad_data = [w.replace(choice(list(w)), choice(["i", "y"])) + choice(["i", "y"])  for w in real_data]
    evaluate_graphmodels(evaluate_nff_words, real_data, bad_data)

def test_no_high_high():
    real_data = get_mandarin_words()
    bad_data = [w.replace(choice(list(w)), "y") + choice(["i", "u"])  for w in real_data]
    evaluate_graphmodels(evaluate_nhh_words, real_data, bad_data)

def test_no_vc():
    real_data = get_mandarin_words()
    bad_data = [w.replace(choice(list(w)), choice(["a", "e", "ɑ", "ə", "u", "y", "i", "o"])+choice(list(w))+choice(cons_ls))  for w in real_data]
    evaluate_graphmodels(evaluate_nvc_real_words, real_data, bad_data)

def test_schwa_roundness():
    real_data = get_mandarin_words()
    bad_data_1 = [w.replace(choice(list(w)), "əu") for w in real_data]
    #bad_data_2 = [w.replace(w[-1], "uə") for w in real_data[int(len(real_data)/2):]]
    #bad_data = bad_data_1 + bad_data_2
    evaluate_graphmodels(evaluate_sro_words, real_data, bad_data_1)

def test_vowel_frontness():
    real_data = get_mandarin_words()
    bad_data_1 = [w.replace(choice(list(w)), choice(["au", "aŋ"])) for w in real_data]
    #bad_data_2 = [w.replace(w[-1], choice(["iə", "yə"])) for w in real_data[int(len(real_data)/2):]]
    #bad_data = bad_data_1 + bad_data_2
    evaluate_graphmodels(evaluate_vfr_words, real_data, bad_data_1)

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
    mask_data = get_masked_mandarin_words(keep_list=["u", "y"])
    bad_data = [w.replace(choice(list(w)), choice(["u", "y"])) + choice(["u", "y"])  for w in mask_data]
    evaluate_graphmodels(evaluate_nll_words, mask_data, bad_data)

def test_no_fro_fro_masked():
    mask_data = get_masked_mandarin_words(keep_list=["i", "y"])
    bad_data = [w.replace(choice(list(w)), choice(["i", "y"])) + choice(["i", "y"])  for w in mask_data]
    evaluate_graphmodels(evaluate_nff_words, mask_data, bad_data)

def test_no_high_high_masked():
    mask_data = get_masked_mandarin_words(keep_list=["i", "u", "y"])
    bad_data = [w.replace(choice(list(w)), "y") + choice(["i", "u"])  for w in mask_data]
    evaluate_graphmodels(evaluate_nhh_words, mask_data, bad_data)

def test_no_vc_masked():
    mask_data = get_masked_mandarin_words(keep_list=["a", "e", "ɑ", "ə", "u", "y", "i", "o", "p", "b", "m", "f", "t", "d", "l", "ts", "tsʰ", "s", "tʂ", "tʂʰ", "ʂ", "ʐ", "tɕ", "tɕʰ", "ɕ", "k", "g", "h"])
    bad_data = [w.replace(choice(list(w)), choice(["a", "e", "ɑ", "ə", "u", "y", "i", "o"])+choice(list(w))+choice(cons_ls))  for w in mask_data]
    evaluate_graphmodels(evaluate_nvc_masked_words, mask_data, bad_data)

def test_schwa_roundness_masked():
    mask_data = get_masked_mandarin_words(keep_list=["ə", "u", "o"])
    bad_data_1 = [w.replace(choice(list(w)), "əu") for w in mask_data]
    #bad_data_2 = [w.replace(w[-1], "uə") for w in mask_data[int(len(mask_data)/2):]]
    #bad_data = bad_data_1 + bad_data_2
    evaluate_graphmodels(evaluate_sro_words, mask_data, bad_data_1)

def test_vowel_frontness_masked():
    mask_data = get_masked_mandarin_words(keep_list=["a", "ə", "e", "ɑ", "i", "y", "n", "u", "ŋ"])
    bad_data_1 = [w.replace(choice(list(w)), choice(["au", "aŋ"])) for w in mask_data]
    #bad_data_2 = [w.replace(w[-1], choice(["iə", "yə"])) for w in mask_data[int(len(mask_data)/2):]]
    #bad_data = bad_data_1 + bad_data_2
    evaluate_graphmodels(evaluate_vfr_words, mask_data, bad_data_1)
