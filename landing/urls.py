
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.RegistroView.as_view(), name='register'),
]

