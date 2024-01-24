from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request, 'Data_Mining/About.html')
def Home(request):
    return render(request, 'Data_Mining/Home.html')