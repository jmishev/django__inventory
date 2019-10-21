from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.GoodCreateView.as_view(), name="main"),
    path('home/', views.Proba, name='home'),
]