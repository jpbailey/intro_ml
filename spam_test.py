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
SPAMDIR = "./test_spam/"
HAMDIR = "./test_ham/"
STOPS = stopwords.words('english')
EXCLUDE = set(string.punctuation) | set(["''", "BR", "--", "/td", "nbsp", "2002", "localhost"])

# bring in the spam only words
with open("./spam_only_words.txt") as f:
    spam_only_words = f.read().splitlines()

# bring in the ham only words
with open("./ham_only_words.txt") as f:
    ham_only_words = f.read().splitlines()

type2_file = open("./type2.txt", 'w')

ham_correct=0
ham_incorrect=0
spam_correct=0
spam_incorrect=0

for (dirpath, dirnames, filenames) in os.walk(SPAMDIR):
	for filename in filenames:
		inputfile=(SPAMDIR + filename)
		with open (inputfile, "r") as myfile:
			s=myfile.read().replace('\n', '')
			s = filter(lambda x: x in string.printable, s)
			wordlist=nltk.word_tokenize(s)
			filtered_words = [i for i in wordlist if (i not in STOPS) and (i not in EXCLUDE)]
			ham_score = (len(list(set(filtered_words) & set(ham_only_words))))
			spam_score = (len(list(set(filtered_words) & set(spam_only_words))))
			if spam_score>ham_score:
				spam_correct+=1
			else:
				spam_incorrect+=1
				for each in filtered_words:
					type2_file.write((each + "\n"))
type2_file.close()
raw_input("Done with spam testing.  Press Enter to continue...")

type1_file = open("./type1.txt", "w")
for (dirpath, dirnames, filenames) in os.walk(HAMDIR):
	for filename in filenames:
		inputfile=(HAMDIR + filename)
		with open (inputfile, "r") as myfile:
			s=myfile.read().replace('\n', '')
			s = filter(lambda x: x in string.printable, s)
			wordlist=nltk.word_tokenize(s)
			filtered_words = [i for i in wordlist if (i not in STOPS) and (i not in EXCLUDE)]
			ham_score = (len(list(set(filtered_words) & set(ham_only_words))))
			spam_score = (len(list(set(filtered_words) & set(spam_only_words))))
			if spam_score>ham_score:
				ham_incorrect+=1
				for each in filtered_words:
					type1_file.write((each + "\n"))
			else:
				ham_correct+=1
raw_input("Done with ham testing.  Press Enter to continue...")
type1_file.close()

print ("Ham accuracy is %f." % (ham_correct/float(ham_correct + ham_incorrect)))
print ("Spam accuracy is %f." % (spam_correct/float(spam_correct + spam_incorrect)))


