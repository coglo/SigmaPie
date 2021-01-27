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
import unittest
from sigmapie.fsm import FSM
from random import randint

'''
def pairs_evaluater(data, Sigma, Gamma):
 
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
    
evaluate_sro_io(generate_sro_io(n=100))
evaluate_vfr_io(generate_vfr_io(n=100))
pairs_evaluater(generate_sro_io(n=100), ["a", "n", "ə", "u"], ["a", "n", "ə", "o", "u"])
pairs_evaluater(generate_vfr_io(n=100), ["a", "ə", "i", "y", "n", "u", "ŋ"], ["a", "ə", "i", "y", "e", "n", "ɑ", "u", "ŋ"])

'''
def test_fst(fst, testdata):
    success, failure = [], []
    n = 0
    for i in testdata:
        if fst.rewrite(i[0]) == i[1]:
            success.append(i)
            n += 1
        else:
            failure.append([i, fst.rewrite(i[0])])
    print("Score:", str(n / len(testdata) * 100) + "%")
    return success, failure

def test_evaluator():
    test_sro = generate_sro_io(n=100, length = 4)
    test_vfr = generate_vfr_io(n = 100, length = 4)
    o_sro = ostia(test_sro, ["a", "n", "ə", "u"], ["a", "n", "ə", "o", "u"])
    o_vfr = ostia(test_vfr, ["a", "ə", "i", "y", "n", "u", "ŋ"], ["a", "ə", "i", "y", "e", "n", "ɑ", "u", "ŋ"])

    success1, failure1 = test_fst(o_sro, test_sro)
    print("Success_sro:", success1[:15])
    print("Failure_sro:", failure1[:15])  

    success2, failure2 = test_fst(o_vfr, test_vfr)
    print("Success_vfr:", success2[:15])
    print("Failure_vfr:", failure2[:15])

    print(len(o_sro.E), len(o_sro.stout))
    print(len(o_vfr.E), len(o_vfr.stout))
