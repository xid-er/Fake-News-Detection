from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def predict(request):
    return render(request, 'main/result.html')