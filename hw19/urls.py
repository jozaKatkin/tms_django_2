from django.urls import path

from hw19.views import index1

urlpatterns = [
    path('index1', index1, name="index1"),
]