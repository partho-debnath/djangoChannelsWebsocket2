from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='index'),
    path('group/', views.ChatView.as_view(), name='chat-view')
]