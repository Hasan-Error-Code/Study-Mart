from django.shortcuts import render

# Create your views here.
def Course(request):
    return render(request, 'Course/Course.html')
def Name(request):
    return render(request, 'Course/Course.html', {'Name': "Hasan"})
def Courses(request):
    course1 = 'Data Mining'
    course2 = 'Machine Learning'
    course3 = 'Django'
    course4 = 'Python'
    Course = {'c1': course1, 'c2': course2, 'c3': course3, 'c4': course4}
    return render(request,'Course/Course.html', Course)