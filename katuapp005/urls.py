from django.conf.urls import url
from django.urls import path
from . import views
# from .views import HelloView, HelloView2, HelloView3, HelloView4, HelloView5

#ジェネリックビュー
from .views import FriendList, FriendDetail


urlpatterns = [
    # path('', HelloView.as_view(), name='index'),
    path('', views.index, name='index'),
    # path('friends', HelloView2.as_view(), name='friends'),
    path('index2', views.index, name='index2'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    #ジェネリックビュー
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
    #検索
    path('find', views.find, name='find'),
    path('check', views.check, name='check'),
]