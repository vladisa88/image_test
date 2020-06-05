from django.urls import path

from . import views


urlpatterns = [
    path('', views.ImageListView.as_view(), name='list'),
    path('<int:pk>/', views.ImageDetailView.as_view(), name='detail'),
    path('upload/', views.ImageCreateView.as_view(), name='create'),
]