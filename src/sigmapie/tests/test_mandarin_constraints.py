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

def test_no_lab_lab():

    data = generate_nll(n=1000)

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
    evaluate_nll_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_nll_words(sl_h.generate_sample(n=1000, repeat=True))
    evaluate_nll_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_nll_words(mtsl_h.generate_sample(n=1000, repeat=True))

def test_no_cor_cor():

    data = generate_ncc(n=1000)

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
    evaluate_ncc_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_ncc_words(sl_h.generate_sample(n=1000, repeat=True))
    evaluate_ncc_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_ncc_words(mtsl_h.generate_sample(n=1000, repeat=True))

def test_no_high_high():

    data = generate_nhh(n=1000)

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
    evaluate_nhh_words(sp_h.generate_sample(n=1000, repeat=True))
    evaluate_nhh_words(sl_h.generate_sample(n=1000, repeat=True))
    evaluate_nhh_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_nhh_words(mtsl_h.generate_sample(n=1000, repeat=True))

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
    evaluate_nvc_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_nvc_words(mtsl_h.generate_sample(n=1000, repeat=True))

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
    evaluate_sro_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_sro_words(mtsl_h.generate_sample(n=1000, repeat=True))

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
    evaluate_vfr_words(tsl_h.generate_sample(n=1000, repeat=True))
    evaluate_vfr_words(mtsl_h.generate_sample(n=1000, repeat=True))

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