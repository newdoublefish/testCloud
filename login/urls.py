from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


from . import views

app_name = 'login'
urlpatterns = [
    url(r'^index', csrf_exempt(views.index), name='login'),
    url(r'^login', csrf_exempt(views.mylogin), name='login'),
]
