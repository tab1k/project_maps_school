from . import views
from django.urls import path

urlpatterns = [
    path('', views.as_view(), name='home'),
    path('subjects', views.subjects),
]
