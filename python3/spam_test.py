"""
Edited April 28, 2016 by Joe Bailey
"""

# import the libraries needed
import os

# define global variables
SPAMDIR = "./test_spam/"
HAMDIR = "./test_ham/"

def GetWordlist(inputfile):
	"""
	Reads in a file as a string and puts it into a list.  Assumes that each line
	is its own word.
	"""
	f = open(inputfile, 'r')
	wordlist = f.read().splitlines()
	f.close()
	return wordlist

def ProcessOneFile(f, hamwords, spamwords):
	"""
	Gets one email in the test set and predicts whether or not it is ham or spam by counting
	the number of words found within each dictionary.
	"""
	wordlist = GetWordlist(f)
	ham_score = (len(list(set(wordlist) & set(hamwords))))
	spam_score = (len(list(set(wordlist) & set(spamwords))))
	if (ham_score > spam_score):
		status = "ham"
	else:
		status = "spam"
	return status

def ProcessDirectory(group, ham_words, spam_words):
	"""
	Goes through a directory of ham or spam and invokes the processing of one email.
	"""
	if group == "ham":
		directory = HAMDIR
	else:
		directory = SPAMDIR
	correct = 0
	incorrect = 0
	for (dirpath, dirnames, filenames) in os.walk(directory):
		for filename in filenames:
			infile = (directory + filename)
			prediction = ProcessOneFile(infile, ham_words, spam_words)
			if prediction == group:
				correct = correct + 1
			else:
				print ("Incorrect prediction with %s." % infile)
				incorrect = incorrect + 1
	return correct, incorrect


def main():
	"""
	This is the main program that invokes the processing of each test directory.
	"""
	spam_words = GetWordlist("./spam_only_words.txt")
	ham_words = GetWordlist("./ham_only_words.txt")
	print ("looking at ham directory")
	correct, incorrect = ProcessDirectory("ham", ham_words, spam_words)
	print ("Results:  %d correct and %d incorrect" % (correct, incorrect))
	print ("looking at the spam directory")
	correct, incorrect = ProcessDirectory("spam", ham_words, spam_words)
	print ("Results:  %d correct and %d incorrect" % (correct, incorrect))

if '__main__' == __name__:
	main()

