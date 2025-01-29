from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]