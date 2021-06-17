from django.conf.urls import url
from django.urls import path
# from . import views
from .views import HelloView, HelloView2


urlpatterns = [
    path('', HelloView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('friends', HelloView2.as_view(), name='friends'),
]