from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('create_meal', views.create_meal, name='create_meal'),
    path('weekplan', views.weekplan, name='weekplan'),
]