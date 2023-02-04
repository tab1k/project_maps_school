from django.shortcuts import render
from django.views.generic import ListView

from subjects.models import Subject
from .forms import ContactForms
from .models import *
# CBV - CLASS BASED VIEWS (ListView)

# Create your views here.

class GeneralPage(ListView):
    model = Category
    template_name = 'main/index.html'
    categories = model.objects.all()
    for category in categories:
        print(category.name)



class Courses(ListView):
    model = Subject
    template_name = 'main/courses.html'

class About(ListView):
    model = Subject
    template_name = 'main/about.html'


class Cooperation(ListView):
    model = Subject
    template_name = 'main/cooperation.html'

class Quotes(ListView):
    model = Subject
    template_name = 'main/quotes.html'

class Contacts(ListView):
    model = Subject
    template_name = 'main/contacts.html'