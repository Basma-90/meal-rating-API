from django.contrib import admin
from django.urls import path
from .views import MealViewSet,RatingViewSet
from django.conf.urls import include
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register('meals',MealViewSet)
routers.register('ratings',RatingViewSet)

urlpatterns = [
    path('',include(routers.urls)),
]
