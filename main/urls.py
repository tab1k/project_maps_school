from . import views
from django.urls import path

urlpatterns = [
    path('', views.general_page, name='home'),
    path('subjects', views.subjects),
]
