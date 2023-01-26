from . import views
from django.urls import path

urlpatterns = [
    path('', views.GeneralPage.as_view(), name='home'),
    path('contacts', views.Contacts.as_view(), name='contacts'),
    path('cooperation', views.Cooperation.as_view(), name='cooperation'),
    path('quotes', views.Quotes.as_view(), name='quotes'),
    path('about', views.About.as_view(), name='about'),
    path('courses', views.Courses.as_view(), name='courses'),
]
