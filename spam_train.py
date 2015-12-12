"""
Edited November 15, 2015 by Joe Bailey
making addditional comments here
"""

# import the libraries needed
import os
import nltk
from nltk.corpus import stopwords
import random
import shutil
import string

# define global variables
STOPS = stopwords.words('english')
EXCLUDE = set(string.punctuation) | set(["''", "BR", "--", "/td", "nbsp", "2002", "localhost"])
SPAMDIR = "./train_spam/"
HAMDIR = "./train_ham/"

hamwords = []
for (dirpath, dirnames, filenames) in os.walk(HAMDIR):
	for filename in filenames:
		inputfile=(HAMDIR + filename)
		with open (inputfile, "r") as myfile:
			s=myfile.read().replace('\n', '')
			s = filter(lambda x: x in string.printable, s)
			wordlist=nltk.word_tokenize(s)
			filtered_words = [i for i in wordlist if (i not in STOPS) and (i not in EXCLUDE)]
			hamwords = hamwords + filtered_words
fdist=nltk.FreqDist(hamwords)
top_list = fdist.most_common(1000)
hamwords=[]
for each in top_list:
	hamwords.append(each[0])
raw_input("Done with ham training.  Press Enter to continue...")

spamwords = []
for (dirpath, dirnames, filenames) in os.walk(SPAMDIR):
	for filename in filenames:
		inputfile=(SPAMDIR + filename)
		with open (inputfile, "r") as myfile:
			s=myfile.read().replace('\n', '')
			s = filter(lambda x: x in string.printable, s)
			wordlist=nltk.word_tokenize(s)
			filtered_words = [i for i in wordlist if (i not in STOPS) and (i not in EXCLUDE)]
			spamwords = spamwords + filtered_words
fdist=nltk.FreqDist(spamwords)
top_list = fdist.most_common(1000)
spamwords=[]
for each in top_list:
	spamwords.append(each[0])
raw_input("Done with spam training.  Press Enter to continue...")

shared_words = list(set(hamwords) & set(spamwords))

ham_only_words = set(hamwords) - set(shared_words)
f = open("./ham_only_words.txt", 'w')
for each in ham_only_words:
	f.write(each + "\n")
f.close()

spam_only_words = set(spamwords) - set(shared_words)
f = open("./spam_only_words.txt", 'w')
for each in spam_only_words:
	f.write(each + "\n")
f.close()

raw_input("Done with training.  Wrote words to ham_only_words.txt and spam_only_words.txt. Press Enter to continue...")

