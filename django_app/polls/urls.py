from django.conf.urls import url

from polls import views

# from . import views와 같음

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
