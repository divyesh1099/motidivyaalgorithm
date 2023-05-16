from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.getAllUserMessages),
    path('<int:id>/', views.getMessageById),
    path('postMessage/', views.postMessage),
    path('deleteMessage/<int:id>/', views.deleteMessage),
]