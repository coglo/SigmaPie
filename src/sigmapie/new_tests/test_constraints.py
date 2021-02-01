import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from sigmapie.generators.no_lab_lab import generate_nll, no_lab_lab, generate_nll_bad, no_lab_lab_bad
from sigmapie.evaluators.no_lab_lab import evaluate_nll_words 
from sigmapie.generators.no_cor_cor import generate_ncc, no_cor_cor, generate_ncc_bad, no_cor_cor_bad
from sigmapie.evaluators.no_cor_cor import evaluate_ncc_words
from sigmapie.generators.no_high_high import generate_nhh, no_high_high, generate_nhh_bad, no_high_high_bad
from sigmapie.evaluators.no_high_high import evaluate_nhh_words
from sigmapie.generators.no_vc import generate_nvc, no_vc, generate_nvc_bad, no_vc_bad
from sigmapie.evaluators.no_vc import evaluate_nvc_words  
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


def test_no_lab_lab_alldata():
    print(generate_nll(n = 10))
    print(generate_nll_bad(n = 10))
    evaluate_nll_words(generate_nll(n = 1000))
    evaluate_nll_words(generate_nll_bad(n = 1000))

def test_no_cor_cor_alldata():
    print(generate_ncc(n = 10))
    print(generate_ncc_bad(n = 10))
    evaluate_ncc_words(generate_ncc(n = 1000))
    evaluate_ncc_words(generate_ncc_bad(n = 1000))

def test_no_high_high_alldata():
    print(generate_nhh(n = 10))
    print(generate_nhh_bad(n = 10))
    evaluate_nhh_words(generate_nhh(n = 1000))
    evaluate_nhh_words(generate_nhh_bad(n = 1000))

def test_no_vc_alldata():
    print(generate_nvc(n = 10))
    print(generate_nvc_bad(n = 10))
    evaluate_nvc_words(generate_nvc(n = 1000))
    evaluate_nvc_words(generate_nvc_bad(n = 1000))

def test_schwa_roundness_alldata():
    print(generate_sro(n = 10))
    print(generate_sro_bad(n = 10))
    evaluate_sro_words(generate_sro(n = 1000))
    evaluate_sro_words(generate_sro_bad(n = 1000))

def test_vowel_frontness_alldata():
    print(generate_vfr(n = 10))
    print(generate_vfr_bad(n = 10))
    evaluate_vfr_words(generate_vfr(n = 1000))
    evaluate_vfr_words(generate_vfr_bad(n = 1000))

 