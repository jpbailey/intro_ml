"""
Edited April 28, 2016 by Joe Bailey
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
EXCLUDE = set(string.punctuation) | set(["''", "BR", "--", "/td", "nbsp", "2002", "localhost", "&nbsp"])

def FilterWord(s):
	"""
	Receives a string and determines whether or not it is a string that should be used
	for analysis (keep = 1) and passes back a clean version of the string.
	"""
	keep = 1 #default is to keep the word
	cleanstring = s.lower()
	drop_chars = ",.:;!"
	for c in drop_chars:
		cleanstring = cleanstring.replace(c, "")
	bad_chars = "><#$/=0123456789+()&*@?"
	for c in bad_chars:
		if cleanstring.find(c)!=-1:
			keep=0
	if len(cleanstring)<3:
		keep=0
	if cleanstring in STOPS:
		keep =0
	if cleanstring in EXCLUDE:
		keep=0
	return keep, cleanstring

def CleanWords(wordlist):
	"""
	Process go go through a list of words and clean each of them up.  Passes back
	a list of clean words.
	"""
	filtered_words =[]
	for each in wordlist:
		flag, cleanstring = FilterWord(each)
		if flag==1:
			filtered_words.append(cleanstring)
	return filtered_words


def SaveWordlist(wordlist, outfile):
	"""
	Saves a list of words to the appropriate file.
	"""
	f = open(outfile, "w")
	for each in wordlist:
		f.write("%s\n" % each)
	f.close()

def GetWordlist(inputfile):
	"""
	Reads in a file as a string and puts it into a list.
	"""
	f = open(inputfile, 'r', encoding="Latin-1")
	s = f.read().replace('\n', '')
	f.close()
	s = ''.join(filter(lambda x: x in string.printable, s))
	wordlist=s.split()
	wordlist = CleanWords(wordlist)
	return wordlist


def DirectorySetup():
	"""
	Sets up the directory structure for output.  We need training and testing
	for both ham and spam examples.
	"""
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
	if not os.path.exists("./train_ham/"):
		os.makedirs("./train_ham/")
	else:
		shutil.rmtree("./train_ham/")
		os.makedirs("./train_ham/")
	if not os.path.exists("./train_spam/"):
		os.makedirs("./train_spam/")
	else:
		shutil.rmtree("./train_spam/")
		os.makedirs("./train_spam/")

def HamProcess():
	"""
	This process goes through the ham email samples, decides whether or not they
	should be used for training or testing, and then puts the words from that
	email into the appropriate folder.
	"""
	train_ham_files = 0
	test_ham_files = 0
	wordlist=[]
	for (dirpath, dirnames, filenames) in os.walk(HAMPATH):
		for filename in filenames:
			if filename != "cmds":
				infile=(HAMPATH + filename)
				random_number = random.uniform(0,1)
				if random_number<TRAIN_PERCENT:
					print ("Ham Training: " + infile)
					outfile=("./train_ham/" + filename)
					SaveWordlist(GetWordlist(infile), outfile)
					train_ham_files = train_ham_files + 1
				else:
					if random_number<(TRAIN_PERCENT + TEST_PERCENT):
						print ("Ham Testing: " + infile)
						outfile=("./test_ham/" + filename)
						SaveWordlist(GetWordlist(infile), outfile)
						test_ham_files = test_ham_files + 1
	print("Ham - training set size is: %d" % train_ham_files)
	print("Ham - testing set size is: %d" % test_ham_files)
	SaveWordlist(wordlist, "./hamwords.txt")
	input("Press Enter to continue...")

def SpamProcess():
	"""
	This routine goes through the spam emails, decides whether or not they are part
	of the training or testing sample, then puts the words from each document in the
	appropriate directory.
	"""
	train_spam_files = 0
	test_spam_files = 0
	wordlist=[]
	for (dirpath, dirnames, filenames) in os.walk(SPAMPATH):
		for filename in filenames:
			if filename != "cmds":
				infile=(SPAMPATH + filename)
				random_number=random.uniform(0,1)
				if random_number<TRAIN_PERCENT:
					print ("Spam Training: " + infile)
					outfile=("./train_spam/" + filename)
					SaveWordlist(GetWordlist(infile), outfile)
					train_spam_files = train_spam_files + 1
				else:
					if random_number<(TRAIN_PERCENT + TEST_PERCENT):
						print ("Spam Testing: " + infile)
						outfile=("./test_spam/" + filename)
						SaveWordlist(GetWordlist(infile), outfile)
						test_spam_files = test_spam_files + 1
	print("Spam - training set size is: %d" % train_spam_files)
	print("Spam - testing set size is: %d" % test_spam_files)
	SaveWordlist(wordlist, "./spamwords.txt")
	input("Press Enter to continue...")

def main():
	"""
	The main part of the script that loops through the input file and processes it
	"""
	DirectorySetup()
	HamProcess()
	SpamProcess()



if '__main__' == __name__:
	main()




