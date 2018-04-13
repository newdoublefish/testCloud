#from django.urls import path
from django.conf.urls import url
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^stubinfo', csrf_exempt(views.stubInfo),name='stubinfo'),
    url(r'^boardinfo', csrf_exempt(views.boardInfo) ,name='boardinfo'),
    url(r'^report', csrf_exempt(views.report),name='report'),
    url(r'^index', csrf_exempt(views.index), name='index'),
    url(r'^data', csrf_exempt(views.getDataAnalysis), name='data'),
]
