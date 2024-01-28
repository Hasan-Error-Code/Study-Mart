from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('c/', views.Course),
    path('n/', views.Name),
    path('ac/', views.Courses)
]
