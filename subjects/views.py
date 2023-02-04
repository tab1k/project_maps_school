from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# CBV - CLASS BASED VIEWS (ListView)



class Python(ListView):
    model = Subject
    template_name = 'subjects/python.html'
    categories = model.objects.all()
    for category in categories:
        print(category.name)



class C_plus(ListView):
    model = Subject
    template_name = 'subjects/c_plus.html'

class Computer_science(ListView):
    model = Subject
    template_name = 'subjects/computer_science.html'


class English(ListView):
    model = Subject
    template_name = 'subjects/english.html'

class Math(ListView):
    model = Subject
    template_name = 'subjects/math.html'

class Web_design(ListView):
    model = Subject
    template_name = 'subjects/web_design.html'