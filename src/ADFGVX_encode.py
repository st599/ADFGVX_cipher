
# LIBRARY IMPORTS
import random

def enc_randomiseAlphabet(verbose):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    l = list(alphabet)
    random.shuffle(l)
    randAlphabet = ''.join(l)
    if verbose:
        print(randAlphabet)
    return(randAlphabet)

def enc_sortKeyword(keyword, verbose):
    l = sorted(keyword)
    sortedKW = ''.join(l)
    if verbose:
        print(keyword, sortedKW)
    return(sortedKW)
