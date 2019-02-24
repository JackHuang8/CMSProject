from django.conf.urls import url

from news import views

urlpatterns = [
    url(r'users/$', views.ListNews.as_view()),
]
