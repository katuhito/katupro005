from django.conf.urls import url
from django.urls import path
from .views import HelloView
# from . import views

urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    # path('', views.index, name='index'),
]