from django.urls import path
from . import views
from .views import upload_picture, delete_image

urlpatterns = [
    path('', views.upload_picture, name='upload'),
    path('delete/', delete_image, name='delete_image'),
]