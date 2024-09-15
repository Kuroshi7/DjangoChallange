from django.urls import path
from .views import index, csv_viewer, image_viewer

urlpatterns = [
    path('', index, name='index'),
    path('csv/', csv_viewer, name='csv_viewer'),
    path('image/', image_viewer, name='image_viewer'),
]