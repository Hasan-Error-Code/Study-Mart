from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Data_Science/Home.html')
def About(request):
    return render(request, 'Data_Science/About.html')