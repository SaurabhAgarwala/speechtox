from django.shortcuts import render, redirect
from .models import Song
from django.http import HttpResponse
from . import forms
import requests
from bs4 import BeautifulSoup
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re, string
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')

# Create your views here.
model = []
for i in range(6):
    filename = './../MLModels/log' + str(i) + str('.sav')
    model.append(pickle.load(open(filename, 'rb')))
vec = pickle.load(open('./../MLModels/vec.pk', 'rb'))
r  = pickle.load(open('./../MLModels/r.pk', 'rb'))
labels = ['Toxic', 'Severe_Toxic', 'Obscene', 'Threat', 'Insult', 'Identity_Hate']



def categorize(request):
    if request.method == 'POST':
        form = forms.SongForm(request.POST)
        if form.is_valid():
            artist = "-".join(list(form.cleaned_data['artist'].lower().split(" ")))
            name = "-".join(list(form.cleaned_data['song_name'].lower().split(" ")))
            query_url = "https://genius.com/" + artist + "-" + name + "-lyrics"
            print(query_url)
            page = requests.get(query_url)
            html = BeautifulSoup(page.text, "html.parser")
            lyricsdiv = html.find("div", class_="lyrics")
            if lyricsdiv != None:
                lyrics = lyricsdiv.get_text()
            else:
                res = "Invalid song/artist."
                return render(request, 'songcategory/output.html', {'op':res})         
            f=0
            rem = []
            for i in range(len(lyrics)):    
                if f==1:
                    if lyrics[i] == ']':
                        f=0
                    continue
                if lyrics[i]=='[':
                    f=1
                    continue
                rem.append(lyrics[i])	
            lyrics = ''.join(rem)
            X_test = [lyrics]
            #X_test = list(X_test)
            #X_test = pd.DataFrame(X_test[0], columns=['comment_text'])
            X_test = vec.transform(X_test)
            result = "The given song is classified as:<br>"
            for i in range(6):
                #filename = './../MLModels/log' + str(i) + str('.sav')
                #model = pickle.load(open(filename, 'rb'))
                pred = model[i].predict(X_test.multiply(r[i]))
                if(pred==1):
                    result += labels[i] + "<br>"
                else:
                    result += ""
            # print(result)
            # and returning a file output.csv which will have the result.
            # f1 = open("./text2category/output.csv", "r")
            # op = f1.read()
            if result == "The given song is classified as:<br>":
                result = "The given song is decent."
        return render(request, 'songcategory/output.html', {'op':result})  
        # return HttpResponse("Done")
    else:
        form = forms.SongForm
    return render(request, 'songcategory/song_details.html', {'form':form})