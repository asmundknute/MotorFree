from django.shortcuts import render, get_object_or_404
from categories.models import Category  # Importar desde la app correcta
from .models import Stream  # Modelo de streaming

def streaming_options(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    streams = Stream.objects.filter(category=category, is_live=True)
    
    context = {
        'category': category,
        'streams': streams
    }
    return render(request, 'streaming/streaming_options.html', context)