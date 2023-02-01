from django.shortcuts import render

from .form import ApiForm
import requests
import json

# Create your views here.
def home_view(request):
    return render(request, 'Mon_api/home_page.html')


    

def consumer(request):
    
    form = ApiForm(request.POST or None)
    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            
            data = json.dumps(form.cleaned_data)
            print(data)
            
            # reponse = requests.post('http://127.0.0.1:8000/predict', data=data)
            reponse = requests.post('https://bsa-api-model.onrender.com/predict', data=data)
            info = reponse.json()["mis_status"]
            if info == 'true':
                info = "Crédit Approuvé"
            else:
                info = "Crédit Refusé"
            return render(request, 'Mon_api/formulaire.html', context={'form' : form, 'info' : info} )

    context = {'form' : form}
    return render(request, 'Mon_api/formulaire.html', context=context )
