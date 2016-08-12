import itertools 

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

get_pledge_list()