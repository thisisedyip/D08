import random

def store_to_dict():
    newdict = {}
    with open('Words.txt', 'r') as lines:
    	for word in lines:
    		key = word.strip()[:len(word)]
    		newdict[key] = "none"
    	return newdict
    		
###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()