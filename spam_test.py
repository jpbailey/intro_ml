"""
Edited November 15, 2015 by Joe Bailey
"""

# define global variables
STOPS = stopwords.words('english')


# import the libraries needed
import os
import nltk
from nltk.corpus import stopwords
import random
import shutil



# need to add more commenting
# need to add more commenting


# now see how well we do applying the model to the test set


# list_of_files = {}
# for (dirpath, dirnames, filenames) in os.walk(HAMPATH):
# 	for filename in filenames:
# 		list_of_files[filename] = os.sep.join([dirpath, filename])
# print(len(list_of_files))

# list_of_files = {}
# for (dirpath, dirnames, filenames) in os.walk(SPAMPATH):
# 	for filename in filenames: 
# 		list_of_files[filename] = os.sep.join([dirpath, filename])
# print(len(list_of_files))
# print(list_of_files)


# for each in list_of_files:
# 	infile=SPAMPATH+each
# 	with open (infile, "r") as myfile:
# 		string=myfile.read().replace('\n', '')
# 		#print type(string)
# 		wordlist=nltk.word_tokenize(string)
# 		filtered_words = [i for i in wordlist if i not in STOPS]
# 		print(filtered_words)
