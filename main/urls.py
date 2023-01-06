from . import views
from django.urls import path

urlpatterns = [
    path('', views.general_page),
    path('subjects', views.subjects),
]
