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
from sigmapie.fst_object import *
from sigmapie.helper import *
from sigmapie.ostia import *

def pairs_evaluater(data, Sigma, Gamma):
    '''
    S = generate_pairs(1500, 5, specifications)
    Sigma = ["a", "o", "A", "b", "p", "B"]
    Gamma = ["a", "o", "b", "p"]
    '''
    T = ostia(data, Sigma, Gamma)

    correct = 0
    for ur,sf in data:
        print(ur, "--->", T.rewrite(ur))
        if T.rewrite(ur) == sf:
            correct += 1

    ratio = (correct / len(data))
    print(f"Percentage of well-formed pairs: {int(ratio * 100)}%.")

    print("States:", T.Q)
    print("State outputs:", T.stout)
    print("\nTransitions:", T.E)

pairs_evaluater(generate_sro_io(n=100), ["a", "n", "ə", "u"], ["a", "n", "ə", "o", "u"])
pairs_evaluater(generate_vfr_io(n=100), ["a", "ə", "i", "y", "n", "u", "ŋ"], ["a", "ə", "i", "y", "e", "n", "ɑ", "u", "ŋ"])
