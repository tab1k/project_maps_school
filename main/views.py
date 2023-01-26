from django.shortcuts import render
from django.views.generic import ListView
from .forms import ContactForms
from .models import *
# CBV - CLASS BASED VIEWS (ListView)

# Create your views here.


def general_page(request):
    return render(request, 'main/index.html')


def subjects(request):

    context = {}

    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            pass


    else:
        pass
        #form = ContactForms()

    context['form'] = form

    return render(request, 'main/courses.html', context=context)
