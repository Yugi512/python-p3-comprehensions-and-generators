#!/usr/bin/env python3

def return_evens(num_list):
    nums = [n for n in num_list if n%2 == 0]
    return nums

def make_exclamation(sentence_list):
    sentence = [(n + "!") for n in sentence_list ]
    return sentence