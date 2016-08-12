#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports
import itertools

# Body
def print_hist_old(h):
    for c in h:
        print(c, h[c])


def print_hist_new(h):
    c = sorted(h.keys(), key=str.lower)
    for words in c:
    	print(str(words)+', '+str(h[words]))
    pass

def getkey(item):
	return item


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


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
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    h = histogram_new(get_pledge_list())
    print_hist_new(h)
    pass

if __name__ == '__main__':
    main()
