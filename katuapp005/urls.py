from django.conf.urls import url
from django.urls import path
from . import views
from .views import HelloView, HelloView2, HelloView3, HelloView4


urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('friends', HelloView2.as_view(), name='friends'),
    path('index2', HelloView3.as_view(), name='index2'),
    path('create', HelloView4.as_view(), name='create'),
]