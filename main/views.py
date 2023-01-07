from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# CBV - CLASS BASED VIEWS (ListView)

# Create your views here.

class General(ListView):
    model = Information_About
    queryset = Information_About.objects.all()
    template_name = 'main/main.html'

#def general_page(request):
    #return render(request, 'main/main.html')


def subjects(request):

    all_subjects = Subject.objects.all()

    for i in all_subjects:
        print(i.name, i.price)

    subject_filters = Subject.objects.filter(price=15000)

    return render(request, 'main/subjects.html')
