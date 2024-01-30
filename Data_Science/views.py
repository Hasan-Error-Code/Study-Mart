from django.shortcuts import render

# Create your views here.
def About(request):
    return render(request, 'Data_Science/About.html')
def Home(request):
    Available_course = {'course': ["Machine Learning", "Data Science", "Django", "Deep Learning", "Data Mining"]}
    return render(request, 'Data_Science/Home.html', Available_course)