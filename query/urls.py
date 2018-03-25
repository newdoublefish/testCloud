#from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^stubinfo', views.stubInfo,name='stubinfo'),
    url(r'^boardinfo', views.boardInfo,name='boardinfo'),
    url(r'^report', views.report,name='report'),
]
