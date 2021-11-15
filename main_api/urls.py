from django.urls import path
from . import views

urlpatterns = [
    path("", views.VideoList.as_view()), 
    # path("display/", views.display)
]
