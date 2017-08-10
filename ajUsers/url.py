from django.conf.urls import include, url
from ajUsers import views

urlpatterns = [
    # fetch all users
    url(r'^fetchAllUsers/', views.UserList.as_view()),

    # user login
    url(r'^user$', views.FetchAjUser.as_view()),
]
