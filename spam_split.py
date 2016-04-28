"""
Edited April 22, 2016 by Joe Bailey
download the corpus from:  http://spamassassin.apache.org/publiccorpus/
in particular you want two files.  the first file should be in
the same directory with this scrips an called "easy_ham":
http://spamassassin.apache.org/publiccorpus/20030228_easy_ham.tar.bz2
the second file you can get from the following url and should be in a directory called "spam":
http://spamassassin.apache.org/publiccorpus/20030228_spam.tar.bz2
not sure why cmds shows up in each of these two directories, but be sure to delete it
"""

# import the libraries needed
import os
import nltk
from nltk.corpus import stopwords
import random
import shutil
import string

# define globl variables here
HAMPATH = "./easy_ham/"
SPAMPATH = "./spam/"
TRAIN_PERCENT = 0.75 # percentage of the corpus used to train
TEST_PERCENT = 0.25  # percentage of the corpus used to test
# note that TRAIN_PERCENT + TEST_PERCENT must be less than or equal to 1
STOPS = stopwords.words("english")
EXCLUDE = set(string.punctuation) | set(["''", "BR", "--", "/td", "nbsp", "2002", "localhost"])

def CleanWords(wordlist):
	filtered_words =[]
	for each in wordlist:
		if [(each not in STOPS) and (each not in EXCLUDE)]:
			if len(each)<20:
				filtered_words.append(each)
	return filtered_words


def SaveWordlist(wordlist, outfile):
	f = open(outfile, "w")
	for each in wordlist:
		f.write("%s\n" % each)
	f.close()

def GetWordlist(inputfile):
	f = open(inputfile, 'r')
	s = f.read().replace('\n', '')
	f.close()
	s = filter(lambda x: x in string.printable, s)
	wordlist=s.split()
	wordlist = CleanWords(wordlist)
	return wordlist


def DirectorySetup():

	if not os.path.exists("./test_ham/"):
		os.makedirs("./test_ham/")
	else:
		shutil.rmtree("./test_ham/")
		os.makedirs("./test_ham/")

	if not os.path.exists("./test_spam/"):
		os.makedirs("./test_spam/")
	else:
		shutil.rmtree("./test_spam/")
		os.makedirs("./test_spam/")

def HamProcess():
	# go through each directory and separate out a training and a testing set
	# first do this for the ham files
	train_ham_files = 0
	test_ham_files = {}
	wordlist=[]
	for (dirpath, dirnames, filenames) in os.walk(HAMPATH):
		for filename in filenames:
			if filename != "cmds":
				infile=(HAMPATH + filename)
				random_number = random.uniform(0,1)
				if random_number<TRAIN_PERCENT:
					print ("Ham Training: " + infile)
					wordlist = wordlist + GetWordlist(infile)
					train_ham_files = train_ham_files + 1
				else:
					if random_number<(TRAIN_PERCENT + TEST_PERCENT):
						print ("Ham Testing: " + infile)
						outfile=("./test_ham/" + filename)
						shutil.copy(infile,outfile)
						test_ham_files[filename] = os.sep.join([dirpath, filename])
	print("Ham - training set size is: %d" % train_ham_files)
	print("Ham - testing set size is: %d" % len(test_ham_files))
	SaveWordlist(wordlist, "./hamwords.txt")
	raw_input("Press Enter to continue...")

def SpamProcess():
	# now do the same thing for the spam files
	train_spam_files = 0
	test_spam_files = {}
	wordlist=[]
	for (dirpath, dirnames, filenames) in os.walk(SPAMPATH):
		for filename in filenames:
			if filename != "cmds":
				infile=(SPAMPATH + filename)
				random_number=random.uniform(0,1)
				if random_number<TRAIN_PERCENT:
					print ("Spam Training: " + infile)
					wordlist = wordlist + GetWordlist(infile)
					train_spam_files = train_spam_files + 1
				else:
					if random_number<(TRAIN_PERCENT + TEST_PERCENT):
						print ("Spam Testing: " + infile)
						outfile=("./test_spam/" + filename)
						shutil.copy(infile,outfile)
						test_spam_files[filename] = os.sep.join([dirpath, filename])
	print("Spam - training set size is: %d" % train_spam_files)
	print("Spam - testing set size is: %d" % len(test_spam_files))
	SaveWordlist(wordlist, "./spamwords.txt")
	raw_input("Press Enter to continue...")

def main():
	"""
	The main part of the script that loops through the input file and processes it
	"""
	DirectorySetup()
	# HamProcess()
	SpamProcess()



if '__main__' == __name__:
	main()




