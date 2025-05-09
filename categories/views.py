from django.shortcuts import render
from .models import Category  # Asegúrate de tener este modelo

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {
        'categories': categories
    })

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'categories/category_detail.html', {
        'category': category
    })