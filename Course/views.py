from django.shortcuts import render

# Create your views here.
def Course(request):
    return render(request, 'Course/Course.html')
def Name(request):
    return render(request, 'Course/Course.html', {'Name': "Hasan"})