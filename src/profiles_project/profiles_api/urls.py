from django.urls import path, re_path
from .views import HelloApiView

urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='hello-api')
]