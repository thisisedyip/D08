#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports
import itertools

# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], [])
        inverse[d[key]].append(key)
    return inverse
    pass


def print_hist_newest(d):
    c = sorted(d.keys())
    count = 1
    for numbers in c:
        while count <= max(d):
            if count == numbers:
                print(str(numbers)+', '+str(d[numbers]))
                count += 1
                break #I don't know why including this break statement makes this function work, but it does...
            else:
                print(str(count)+', '+'[]')
                count += 1 
    pass

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_new(s):
    d = dict()
    count = 0
    for c in s:
        count = d.get(c, 0)
        d[c] = count + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    pledge_list = []
    with open('pledge.txt', 'r') as pledge:
        for words in pledge:
            pledge_list.append(words.split())
        flat_pledge_list = list(itertools.chain(*pledge_list))
        return flat_pledge_list
    pass
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
