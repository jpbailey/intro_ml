"""
Edited November 15, 2015 by Joe Bailey
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
import random
import shutil

# define globl variables here
HAMPATH = "./easy_ham/"
SPAMPATH = "./spam/"
TRAIN_PERCENT = 0.05 # percentage of the corpus used to train
TEST_PERCENT = 0.05  # percentage of the corpus used to test
# note that TRAIN_PERCENT + TEST_PERCENT must be less than or equal to 1

if not os.path.exists("./train_ham/"):
	os.makedirs("./train_ham/")
else:
	shutil.rmtree("./train_ham/")
	os.makedirs("./train_ham/")

if not os.path.exists("./test_ham/"):
	os.makedirs("./test_ham/")
else:
	shutil.rmtree("./test_ham/")
	os.makedirs("./test_ham/")

if not os.path.exists("./train_spam/"):
	os.makedirs("./train_spam/")
else:
	shutil.rmtree("./train_spam/")
	os.makedirs("./train_spam/")

if not os.path.exists("./test_spam/"):
	os.makedirs("./test_spam/")
else:
	shutil.rmtree("./test_spam/")
	os.makedirs("./test_spam/")

# go through each directory and separate out a training and a testing set
# first do this for the ham files
train_ham_files = {}
test_ham_files = {}
for (dirpath, dirnames, filenames) in os.walk(HAMPATH):
	for filename in filenames:
		if filename != "cmds":
			infile=(HAMPATH + filename)
			random_number = random.uniform(0,1)
			if random_number<TRAIN_PERCENT:
				outfile=("./train_ham/" + filename)
				shutil.copy(infile,outfile)
				train_ham_files[filename] = os.sep.join([dirpath, filename])
			else:
				if random_number<(TRAIN_PERCENT + TEST_PERCENT):
					outfile=("./test_ham/" + filename)
					shutil.copy(infile,outfile)
					test_ham_files[filename] = os.sep.join([dirpath, filename])
print("Ham - training set size is: %d" % len(train_ham_files))
print("Ham - testing set size is: %d" % len(test_ham_files))
raw_input("Press Enter to continue...")

# now do the same thing for the spam files
train_spam_files = {}
test_spam_files = {}
for (dirpath, dirnames, filenames) in os.walk(SPAMPATH):
	for filename in filenames:
		if filename != "cmds":
			infile=(SPAMPATH + filename)
			random_number=random.uniform(0,1)
			if random_number<TRAIN_PERCENT:
				outfile=("./train_spam/" + filename)
				shutil.copy(infile,outfile)
				train_spam_files[filename] = os.sep.join([dirpath, filename])
			else:
				if random_number<(TRAIN_PERCENT + TEST_PERCENT):
					outfile=("./test_spam/" + filename)
					shutil.copy(infile,outfile)
					test_spam_files[filename] = os.sep.join([dirpath, filename])
print("Spam - training set size is: %d" % len(train_spam_files))
print("Spam - testing set size is: %d" % len(test_spam_files))
raw_input("Press Enter to continue...")






