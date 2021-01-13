from sigmapie.generators.high_high import generate_wfd, word_final_devoicing
from sigmapie.evaluators.high_high import evaluate_wfd_words, evaluate_wfd_pairs
from sigmapie.sp_class import SP
from sigmapie.sl_class import SL
from sigmapie.tsl_class import TSL
from sigmapie.mtsl_class import MTSL

def test_high_high():
    evaluate_wfd_words(generate_wfd(n = 1000, pairs = False))
    evaluate_wfd_pairs(generate_wfd(n = 1000, pairs = True))


def test_high_high_sp():
    data = generate_wfd(n=1000, pairs=False)

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

    evaluate_wfd_words(sp_h.generate_sample(n=1000))
    evaluate_wfd_words(sl_h.generate_sample(n=1000))
    evaluate_wfd_words(tsl_h.generate_sample(n=1000))
    evaluate_wfd_words(mtsl_h.generate_sample(n=1000))
    