from django.shortcuts import render
from django import forms
import requests

# Create your views here.
def home_view(request):
    return render(request, 'Mon_api/home_page.html')


class PredictionForm(forms.Form):
    state = forms.CharField()
    bankstate =forms.CharField()
    naics =  forms.CharField()
    term = forms.CharField()
    noemp = forms.CharField()
    newexist = forms.CharField()
    createjob = forms.CharField()
    retainedjob = forms.CharField()
    franchisecode = forms.CharField()
    urbanrural = forms.CharField()
    revlinecr = forms.CharField()
    lowdoc = forms.CharField()
    grappv = forms.CharField()
    

def api_prediction(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            #ajouter les champs necessaire
            data = form.cleaned_data
            age = data['age']
            sex = data['sex']
            city = data['city']
            url = 'https://api.example.com/predict'
            payload = {'age': age, 'sex': sex, 'city': city}
            response = requests.get(url, params=payload)
            prediction = response.json()['prediction']
            return render(request, 'api.html', {'prediction': prediction})
    else:
        form = PredictionForm()
    return render(request, 'Mon_api/api.html', {'form': form})
