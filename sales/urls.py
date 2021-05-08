from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.fully, name='fully'),
    path('fully', views.fully, name="fully"),
    path('partially', views.partially, name="partially"),
    path('cannotbe', views.cannotbe, name="cannotbe")
]