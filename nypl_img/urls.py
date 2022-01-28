from django.urls import path
from . import views

urlpatterns = [
    path('randomimg/<str:date>/', views.img_capture, name='img_capture')
]