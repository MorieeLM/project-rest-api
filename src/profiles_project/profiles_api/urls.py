from django.urls import path, re_path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name='hello-api'),
    path('', include(router.urls))
]

