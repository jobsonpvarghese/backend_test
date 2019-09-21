from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='Asthra-home'),
    path('about/', views.about, name='Asthra-about'),
]