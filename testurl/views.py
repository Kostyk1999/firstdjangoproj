from django.shortcuts import render

# Create your views here.
def home(request, num):
    return render(request, 'home.html', {})