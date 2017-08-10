from django.conf.urls import url
from . import views

urlpatterns = [
    # /ajUsers/
    url(r'^$', views.index, name='index'),

    # /ajUsers/1
    url(r'^(?P<phoneNumber>[0-9]+)/$', views.detail, name='detail')
]
