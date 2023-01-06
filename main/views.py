from django.shortcuts import render


# Create your views here.


def general_page(request):
    return render(request, 'main/main.html')


def subjects(request):
    return render(request, 'main/subjects.html')
