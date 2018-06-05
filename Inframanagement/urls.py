from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url('^$', views.index, name='index'),
    url('login/$', login , {'template_name' : 'Inframanagement/login.html'}),
]
