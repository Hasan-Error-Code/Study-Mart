from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Deep_Learning/Home.html')
def About(request):
    return render(request, 'Deep_Learning/About.html')
    