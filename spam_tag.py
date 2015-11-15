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

# find the top 100 words in the spam and ham train directories

# remove the intersection set

# print out a dictionary where spam entry gets a +1 and each ham entry gets a -1