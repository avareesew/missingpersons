from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here

def indexPageView(request):
    return render(request, 'missingpersonsapp/index.html')

def statisticsPageView(request):
    return render(request, 'missingpersonsapp/statistics.html')
def bePresentPageView(request):
    return render(request, 'missingpersonsapp/bepresent.html')
def resourcesPageView(request):
    return render(request, 'missingpersonsapp/resources.html')