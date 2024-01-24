from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Data_Science/home.html')
def About(request):
    return render(request, 'Data_Science/about.html')