from django.shortcuts import render, redirect
from .models import Content
from django.http import HttpResponse
from . import forms
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re, string
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
# from speechtox.MLModels.ml import label

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = forms.InputForm(request.POST)
        if form.is_valid():
    #         ans = label(form.cleaned_data['body'])
            vec = pickle.load(open('./../MLModels/vec.pk', 'rb'))
            X_test = [form.cleaned_data['body']]
            X_test = vec.transform(X_test)

            r  = pickle.load(open('./../MLModels/r.pk', 'rb'))

            labels = ['Toxic', 'Severe_Toxic', 'Obscene', 'Threat', 'Insult', 'Identity_Hate']
            result = "The entered text is classified as: "
            for i in range(6):
                filename = './../MLModels/log' + str(i) + str('.sav')
                model = pickle.load(open(filename, 'rb'))
                pred = model.predict(X_test.multiply(r[i]))
                if(pred==1):
                    result += labels[i] + " "
            if result == "The entered text is classified as: ":
                result = "The entered text is decent."
        #     result = ans
        return render(request, 'text2category/output.html', {'op':result})  
    else:
        form = forms.InputForm
    return render(request, 'text2category/input_create.html', {'form':form})