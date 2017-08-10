from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('ajUsers.url')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
