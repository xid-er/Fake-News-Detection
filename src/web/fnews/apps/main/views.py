from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def prediction(request):
    return render(request, 'main/prediction.html')