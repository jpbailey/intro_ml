"""
Edited April 28, 2016 by Joe Bailey
"""

# import the libraries needed
import os
import nltk
from nltk.corpus import stopwords
import random
import shutil
import string

# define global variables
STOPS = stopwords.words("english")
EXCLUDE = set(string.punctuation) | set(["''", "BR", "--", "/td", "nbsp", "2002", "localhost"])
SPAMDIR = "./train_spam/"
HAMDIR = "./train_ham/"


def GetUniqueWords(set_one, set_two):
	"""
	Two distinct lists are passed and the intersection of the two sets are removed.
	"""
	clean_one=[]
	clean_two=[]
	for each in set_one:
		if each not in set_two:
			clean_one.append(each)
	for each in set_two:
		if each not in set_one:
			clean_two.append(each)
	return clean_one, clean_two

def GetWordlist(inputfile):
	"""
	Reads in a file as a string and puts it into a list.  Assumes that each line
	is its own word.
	"""
	f = open(inputfile, 'r')
	wordlist = f.read().splitlines()
	return wordlist

def SaveWordlist(wordlist, outfile):
	"""
	Saves a list of words to the appropriate file.
	"""
	f = open(outfile, "w")
	for each in wordlist:
		f.write("%s\n" % each)
	f.close()

def GetDirWords(directory):
	"""
	Reads in all of the words found within all the files within a directory.
	"""
	words = []
	for (dirpath, dirnames, filenames) in os.walk(directory):
		for filename in filenames:
			inputfile=(directory + filename)
			wordlist = GetWordlist(inputfile)
			words = words + wordlist
	fdist=nltk.FreqDist(words)
	top_list = fdist.most_common(1000)
	words=[]
	for each in top_list:
		words.append(each[0])
	return words

def main():
	"""
	The main part of the script that loops through the input file and processes it
	"""
	print ("Processing ham training sample.")
	hamwords = GetDirWords(HAMDIR)
	raw_input("Press Enter to continue...")
	print ("Processing spam training sample.")
	spamwords = GetDirWords(SPAMDIR)
	raw_input("Press Enter to continue...")
	ham_only, spam_only = GetUniqueWords(hamwords, spamwords)
	SaveWordlist(ham_only, "./ham_only_words.txt")
	SaveWordlist(spam_only, "./spam_only_words.txt")	


if '__main__' == __name__:
	main()

