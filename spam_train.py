"""
Edited November 15, 2015 by Joe Bailey
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



# find the top 100 words in the spam and ham train directories

hamwords = []
for (dirpath, dirnames, filenames) in os.walk(HAMDIR):
	for filename in filenames:
		inputfile=(HAMDIR + filename)
		with open (inputfile, "r") as myfile:
			s=myfile.read().replace('\n', '')
			s = filter(lambda x: x in string.printable, s)
			wordlist=nltk.word_tokenize(s)
			filtered_words = [i for i in wordlist if (i not in STOPS) and (i not in EXCLUDE)]
			# print type(filtered_words)
			hamwords = hamwords + filtered_words
			# print(hamwords)
			# fdist=nltk.FreqDist(filtered_words)
			# print fdist.most_common(100)
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
			# fdist=nltk.FreqDist(filtered_words)
			# print fdist.most_common(100)
raw_input("Done with spam training.  Press Enter to continue...")

print "most common 10 ham words"
print type(hamwords)
fdist1=nltk.FreqDist(hamwords)
print fdist1.most_common(10)

print "most common 10 spam words"
fdist2=nltk.FreqDist(spamwords)
print fdist2.most_common(10)

# remove the intersection set

# print out a dictionary where spam entry gets a +1 and each ham entry gets a -1