from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
]