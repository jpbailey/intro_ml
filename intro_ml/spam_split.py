import os
import random
import shutil

# download the corpus from:  http://spamassassin.apache.org/publiccorpus/
# http://spamassassin.apache.org/publiccorpus/20030228_easy_ham.tar.bz2
# http://spamassassin.apache.org/publiccorpus/20030228_spam.tar.bz2

# need to add more commenting


# define globl variables here
HAMPATH = "./ham/"
SPAMPATH = "./spam/"
STOPS = stopwords.words('english')
SPLIT = 0.6 # percentage of the universe one uses to split the sample to train or test

if not os.path.exists("./train-ham/"):
	os.makedirs("./train-ham/")
else:
	shutil.rmtree("./train-ham/")
	os.makedirs("./train-ham/")

if not os.path.exists("./test-ham/"):
	os.makedirs("./test-ham/")
else:
	shutil.rmtree("./test-ham/")
	os.makedirs("./test-ham/")

if not os.path.exists("./train-spam/"):
	os.makedirs("./train-spam/")
else:
	shutil.rmtree("./train-spam/")
	os.makedirs("./train-spam/")

if not os.path.exists("./test-spam/"):
	os.makedirs("./test-spam/")
else:
	shutil.rmtree("./test-spam/")
	os.makedirs("./test-spam/")

# go through each directory and separate out a training and a testing set
# first do this for the ham files
train_ham_files = {}
test_ham_files = {}
for (dirpath, dirnames, filenames) in os.walk(HAMPATH):
	for filename in filenames:
		infile=(HAMPATH + filename)
		if random.uniform(0,1)<SPLIT:
			outfile=("./train-ham/" + filename)
			shutil.copy(infile,outfile)
			train_ham_files[filename] = os.sep.join([dirpath, filename])
		else:
			outfile=("./test-ham/" + filename)
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
			outfile=("./train-spam/" + filename)
			shutil.copy(infile,outfile)
			train_spam_files[filename] = os.sep.join([dirpath, filename])
		else:
			outfile=("./test-spam/" + filename)
			shutil.copy(infile,outfile)
			test_spam_files[filename] = os.sep.join([dirpath, filename])
print("the percent of files in the training set are:")
print(len(train_spam_files)/float(len(train_spam_files)+len(test_spam_files)))
raw_input("Press Enter to continue...")






