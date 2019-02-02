from django.shortcuts import render, redirect
from .models import Content
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = forms.InputForm(request.POST)
        # e_url = request.POST.get('slug')
        if form.is_valid():
            f = open(form.cleaned_data['ipfn'], "w")
            f.write(form.cleaned_data['body'])
            # s_instance = form.save(commit=False)
            # s_instance.slug =  e_url
            # s_instance.save()
        # return render(request, 'text2category/post_url.html', {'e_url':e_url})  
        return HttpResponse("Done")
    else:
        form = forms.InputForm
    # pastes = Content.objects.all()
    # pastes = sorted(pastes,key=lambda x:x.date,reverse=True)
    return render(request, 'text2category/input_create.html', {'form':form})