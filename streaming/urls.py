from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/', views.streaming_options, name='streaming_options'),
]