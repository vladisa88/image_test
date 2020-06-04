from django.urls import path

from . import views


urlpatterns = [
    path('', views.ImageListView.as_view(), name='list'),
    path('upload/', views.ImageCreateView.as_view(), name='create'),
]