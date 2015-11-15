"""
Edited November 15, 2015 by Joe Bailey
download the corpus from:  http://spamassassin.apache.org/publiccorpus/
in particular you want two files.  the first file should be in
the same directory with this scrips an called "easy_ham":
http://spamassassin.apache.org/publiccorpus/20030228_easy_ham.tar.bz2
the second file you can get from the following url and should be in a directory called "spam":
http://spamassassin.apache.org/publiccorpus/20030228_spam.tar.bz2
"""

# define globl variables here
HAMPATH = "./easy_ham/"
SPAMPATH = "./spam/"
SPLIT = 0.6 # percentage of the universe one uses to split the sample to train or test


# import the libraries needed
import os
import random
import shutil


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
		infile=(HAMPATH + filename)
		if random.uniform(0,1)<SPLIT:
			outfile=("./train_ham/" + filename)
			shutil.copy(infile,outfile)
			train_ham_files[filename] = os.sep.join([dirpath, filename])
		else:
			outfile=("./test_ham/" + filename)
			shutil.copy(infile,outfile)
			test_ham_files[filename] = os.sep.join([dirpath, filename])
print("the percent of files in the training set are:")
print(len(train_ham_files)/float(len(train_ham_files)+len(test_ham_files)))
raw_input("Press Enter to continue...")

# now do the same thing for the spam files
train_spam_files = {}
test_spam_files = {}
for (dirpath, dirnames, filenames) in os.walk(SPAMPATH):
	for filename in filenames:
		infile=(SPAMPATH + filename)
		if random.uniform(0,1)<SPLIT:
			outfile=("./train_spam/" + filename)
			shutil.copy(infile,outfile)
			train_spam_files[filename] = os.sep.join([dirpath, filename])
		else:
			outfile=("./test_spam/" + filename)
			shutil.copy(infile,outfile)
			test_spam_files[filename] = os.sep.join([dirpath, filename])
print("the percent of files in the training set are:")
print(len(train_spam_files)/float(len(train_spam_files)+len(test_spam_files)))
raw_input("Press Enter to continue...")






