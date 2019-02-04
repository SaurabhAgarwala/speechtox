import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re, string
import requests
from bs4 import BeautifulSoup
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')

labels = ['Toxic', 'Severe Toxic', 'Obscene', 'Threat', 'Insult', 'Identity Hate']

model=[]
for i in range(6):
     filename = 'log' + str(i) + str('.sav')
     model.append(pickle.load(open(filename, 'rb')))

vec = pickle.load(open('vec.pk', 'rb'))
r  = pickle.load(open('r.pk', 'rb'))

def tokenize(s):
        return re_tok.sub(r' \1 ', s).split()

def label(content):
    X_test = [content]
    X_test = vec.transform(X_test)
    result = ""
    for i in range(6):
        pred = model[i].predict(X_test.multiply(r[i]))
        if(pred==1):
            result += labels[i] + " "
    return result    
