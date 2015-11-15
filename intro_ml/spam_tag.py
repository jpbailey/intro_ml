import os
import nltk
from nltk.corpus import stopwords
import random
import shutil

STOPS = stopwords.words('english')

# need to add more commenting

# find the top 100 words in the spam and ham train directories

# remove the intersection set

# print out a dictionary where spam entry gets a +1 and each ham entry gets a -1