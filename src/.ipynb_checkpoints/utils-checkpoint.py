import pandas as pd
import pandas as pd
import numpy as np
import nltk
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
nltk.download('stopwords')


stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()
string.punctuation
    
def clean_message(message):
    message = "".join([word for word in message if word not in string.punctuation])
    tokens = re.split('\W+', message)
    message = [ps.stem(word.lower()) for word in tokens if word not in stopwords]
    return message

