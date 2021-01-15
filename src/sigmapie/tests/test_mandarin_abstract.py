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

def evaluate_models(evaluator, data):
    
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
    evaluator(sp_h.generate_sample(n=1000, repeat=True))
    evaluator(sl_h.generate_sample(n=1000, repeat=True))
    evaluator(tsl_h.generate_sample(n=1000, repeat=True))
    evaluator(mtsl_h.generate_sample(n=1000, repeat=True))
    
    print("SL k:", sl_h.k)

    print("SL sample:", sl_h.generate_sample(20, repeat=False), "\n")
    print("SP sample:", sp_h.generate_sample(20, repeat=False), "\n")
    print("TSL tier:", tsl_h.tier)
    print("TSL sample:", tsl_h.generate_sample(20, repeat=False), "\n")
    print("MTSL tiers:", mtsl_h.tier)
    print("MTSL sample:", mtsl_h.generate_sample(20, repeat=False))

    print("SP alphabet:", sp_h.alphabet)
    print("SL alphabet:", sl_h.alphabet)
    print("TSL alphabet:", tsl_h.alphabet)
    print("MTSL alphabet:", mtsl_h.alphabet)
    print("SP alphabet:", sp_h.grammar)
    print("SL alphabet:", sl_h.grammar)
    print("TSL alphabet:", tsl_h.grammar)
    print("MTSL alphabet:", mtsl_h.grammar)
    print("SP alphabet:", sp_h.check_polarity())
    print("SL alphabet:", sl_h.check_polarity())
    print("TSL alphabet:", tsl_h.check_polarity())
    print("MTSL alphabet:", mtsl_h.check_polarity())
    print("MTSL tiers:", mtsl_h.tier)

def test_no_lab_lab():
    evaluate_models(evaluate_nll_words, generate_nll(n=1000))

def test_no_cor_cor():
    evaluate_models(evaluate_ncc_words, generate_ncc(n=1000))

def test_no_high_high():
    evaluate_models(evaluate_nhh_words, generate_nhh(n=1000))

def test_no_vc():

    data = generate_nvc(n=1000)

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
    evaluate_nvc_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_nvc_words(sl_h.generate_sample(n=1000, repeat=True))
    #evaluate_nvc_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_nvc_words(mtsl_h.generate_sample(n=1000, repeat=True))
    print("SP alphabet:", sp_h.alphabet)
    print("SL alphabet:", sl_h.alphabet)
    print("TSL alphabet:", tsl_h.alphabet)
    print("MTSL alphabet:", mtsl_h.alphabet)
    print("SP alphabet:", sp_h.grammar)
    print("SL alphabet:", sl_h.grammar)
    print("TSL alphabet:", tsl_h.grammar)
    print("MTSL alphabet:", mtsl_h.grammar)
    print("SP alphabet:", sp_h.check_polarity())
    print("SL alphabet:", sl_h.check_polarity())
    print("TSL alphabet:", tsl_h.check_polarity())
    print("MTSL alphabet:", mtsl_h.check_polarity())
    print("MTSL tiers:", mtsl_h.tier)

def test_schwa_roundness():

    data = generate_sro(n=1000)

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
    evaluate_sro_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_words(sl_h.generate_sample(n=1000, repeat=True))
    #evaluate_sro_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_words(mtsl_h.generate_sample(n=1000, repeat=True))
    print("SP alphabet:", sp_h.alphabet)
    print("SL alphabet:", sl_h.alphabet)
    print("TSL alphabet:", tsl_h.alphabet)
    print("MTSL alphabet:", mtsl_h.alphabet)
    print("SP alphabet:", sp_h.grammar)
    print("SL alphabet:", sl_h.grammar)
    print("TSL alphabet:", tsl_h.grammar)
    print("MTSL alphabet:", mtsl_h.grammar)
    print("SP alphabet:", sp_h.check_polarity())
    print("SL alphabet:", sl_h.check_polarity())
    print("TSL alphabet:", tsl_h.check_polarity())
    print("MTSL alphabet:", mtsl_h.check_polarity())
    print("MTSL tiers:", mtsl_h.tier)
'''
def test_schwa_roundness_io():

    data = generate_sro_io(n=1000)

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

    evaluate_sro_io(data)
    evaluate_sro_io(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_io(sl_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_io(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_io(mtsl_h.generate_sample(n=1000, repeat=True))
'''
def test_vowel_frontness():

    data = generate_vfr(n=1000)

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
    evaluate_vfr_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_words(sl_h.generate_sample(n=1000, repeat=True))
    #evaluate_vfr_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_words(mtsl_h.generate_sample(n=1000, repeat=True))
    print("SP alphabet:", sp_h.alphabet)
    print("SL alphabet:", sl_h.alphabet)
    print("TSL alphabet:", tsl_h.alphabet)
    print("MTSL alphabet:", mtsl_h.alphabet)
    print("SP alphabet:", sp_h.grammar)
    print("SL alphabet:", sl_h.grammar)
    print("TSL alphabet:", tsl_h.grammar)
    print("MTSL alphabet:", mtsl_h.grammar)
    print("SP alphabet:", sp_h.check_polarity())
    print("SL alphabet:", sl_h.check_polarity())
    print("TSL alphabet:", tsl_h.check_polarity())
    print("MTSL alphabet:", mtsl_h.check_polarity())
    print("MTSL tiers:", mtsl_h.tier)

'''
def test_vowel_frontness_io():

    data = generate_vfr_io(n=1000)

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

    evaluate_vfr_io(data)
    evaluate_vfr_io(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_io(sl_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_io(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_io(mtsl_h.generate_sample(n=1000, repeat=True))
'''