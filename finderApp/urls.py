from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup, name="signup"),
    url(r'^index$', views.index, name="index"),
    url(r'^index2$', views.index2, name="index2"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^(?P<todo_id>[0-9]+)/done/$', views.done, name='done'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
