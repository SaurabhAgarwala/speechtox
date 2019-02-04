from django.shortcuts import render, redirect
from .models import NumberOfSongs
from django.http import HttpResponse
from . import forms
import requests
import billboard
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
chart = billboard.ChartData('hot-100')
l=['&','Featuring',',','X']


def playlist_categorize(request):
    glt=[]
    gla=[]
    blt=[]
    bla=[]
    nlt=[]
    nla=[]
    if request.method == 'POST':
        form = forms.NumberOfSongsForm(request.POST)
        if form.is_valid():
            for i in range(form.cleaned_data['number_of_songs']):
                found=False
                song = chart[i]
                title = song.title
                artist = song.artist
                for x in l:
                    if(x in artist):
                        artist=artist[:artist.index(x)]
                artist.replace('+', ' ')
                artist = artist.lstrip()
                
                artist = "-".join(list(artist.lower().split()))
                title = "-".join(list(title.lower().split()))
                query_url = "https://genius.com/" + artist + "-" + title + "-lyrics"
                print("x",query_url,"x")
                '''
                song=chart[i]
                title=song.title
                if '(' in title:
                    i=title.index('(')
                    title=title[:i]
                title=title.replace('&',' ')
                art=song.artist
                art.split()
                for s in l:
                    if s in art:
                        i=art.index(s)
                        art=art[i]
                art.replace(' + ',' ')
                #print(title,": ",artist)

                artist = "-".join(list(art.lower().split(" ")))
                name = "-".join(list(title.lower().split(" ")))
                query_url = "https://genius.com/" + artist + "-" + name + "-lyrics"
                print(query_url)
                '''
                page = requests.get(query_url)
                html = BeautifulSoup(page.text, "html.parser")
                lyricsdiv = html.find("div", class_="lyrics")
                if lyricsdiv != None:
                    lyrics = lyricsdiv.get_text()
                else:
                    nlt.append(title)
                    nla.append(artist)
                    continue
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
                X_test = vec.transform(X_test)
                for i in range(6):
                    pred = model[i].predict(X_test.multiply(r[i]))
                    if(pred==1):
                        found=True
                        break
                if found==True:
                    blt.append(title)
                    bla.append(artist)
                else:
                    glt.append(title)
                    gla.append(artist)
            gl=""
            bl=""
            nl=""
            for i in range(len(glt)):
                gl+=glt[i] + " by " + gla[i] + "<br>"
            for i in range(len(blt)):
                bl+=blt[i] + " by " + bla[i] + "<br>"
            for i in range(len(nlt)):
                nl+=nlt[i] + " by " + nla[i] + "<br>"
        return render(request, 'playlistcategorize/output.html', {'gl':gl, 'bl':bl, 'nl':nl})  
    else:
        form = forms.NumberOfSongsForm
    return render(request, 'playlistcategorize/input.html', {'form':form})