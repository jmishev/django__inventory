from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.GoodCreateView.as_view(), name="main"),
    path('end/', views.end, name='end'),
    path('download/', views.download, name='download'),
    path('delete/', views.delete, name='delete'),

 ]