from sigmapie.generators.no_lab_lab import generate_nll, no_lab_lab, generate_nll_bad, no_lab_lab_bad
from sigmapie.evaluators.no_lab_lab import evaluate_nll_words 
from sigmapie.generators.no_cor_cor import generate_ncc, no_cor_cor, generate_ncc_bad, no_cor_cor_bad
from sigmapie.evaluators.no_cor_cor import evaluate_ncc_words
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
import pytest


def evaluate_models(evaluator, data, datan, tsl=True):
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

    #evaluator(data)

    evaluator(sl_h.generate_sample(n=1000, repeat=True))
    evaluator(sp_h.generate_sample(n=1000, repeat=True))
    if tsl:
        evaluator(tsl_h.generate_sample(n=1000, repeat=True))
    evaluator(mtsl_h.generate_sample(n=1000, repeat=True))


    '''
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
    '''
    print("test data")
    print("SL", sl_h.percent_grammatical(data))
    print("SP", sp_h.percent_grammatical(data))
    print("TSL", tsl_h.percent_grammatical(data))
    print("MTSL", mtsl_h.percent_grammatical(data))

    #print(datan[0:20], "\n")
    #evaluator(datan)
    
    print("Non word data")
    print("SL", sl_h.percent_grammatical(datan))
    print("SP", sp_h.percent_grammatical(datan))
    print("TSL", tsl_h.percent_grammatical(datan))
    print("MTSL", mtsl_h.percent_grammatical(datan))
 


def test_no_lab_lab_generated():
    evaluate_models(evaluate_nll_words, generate_nll(n=1000), generate_nll_bad(n=1000))

def test_no_cor_cor_generated():
    evaluate_models(evaluate_ncc_words, generate_ncc(n=1000), generate_ncc_bad(n=1000))

def test_no_high_high_generated():
    evaluate_models(evaluate_nhh_words, generate_nhh(n=1000), generate_nhh_bad(n=1000))

def test_no_vc_generated():
    evaluate_models(evaluate_nvc_words, generate_nvc(n=1000), generate_nvc_bad(n=1000))

def test_schwa_roundness_generated():
    evaluate_models(evaluate_sro_words, generate_sro(n=1000), generate_sro_bad(n=1000))

def test_vowel_frontness_generated():
    evaluate_models(evaluate_vfr_words, generate_vfr(n=1000), generate_vfr_bad(n=1000))


    '''
    sl_h.switch_polarity()
    print("Polarity of the SL grammar:", sl_h.check_polarity())
    print("SL grammar:", sl_h.grammar)
    sp_h.switch_polarity()
    print("Polarity of the SP grammar:", sp_h.check_polarity())
    print("SP grammar:", sp_h.grammar)
    tsl_h.switch_polarity()
    print("Polarity of the TSL grammar:", tsl_h.check_polarity())
    print("TSL grammar:", tsl_h.grammar)
    mtsl_h.switch_polarity()
    print("Polarity of the MTSL grammar:", mtsl_h.check_polarity())
    '''


'''
def test_no_lab_lab():
    evaluate_models(evaluate_nll_words, generate_nll(n=1000))

def test_no_cor_cor():
    evaluate_models(evaluate_ncc_words, generate_ncc(n=1000))

def test_no_high_high():
    evaluate_models(evaluate_nhh_words, generate_nhh(n=1000))

def test_no_vc():
    evaluate_models(evaluate_nvc_words, generate_nvc(n=1000))

def test_schwa_roundness():
    evaluate_models(evaluate_sro_words, generate_sro(n=1000), tsl=False)

@pytest.mark.skip(reason="no way of currently testing this")
def test_schwa_roundness_io():
    evaluate_models(evaluate_sro_io, generate_sro_io(n=1000))

def test_vowel_frontness():
    evaluate_models(evaluate_vfr_words, generate_vfr(n=1000))

@pytest.mark.skip(reason="no way of currently testing this")
def test_vowel_frontness_io():
    evaluate_models(evaluate_vfr_io, generate_vfr_io(n=1000))
'''