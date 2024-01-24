from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Machine_Learning/Home.html')
def About(request):
    return render(request, 'Machine_Learning/About.html')