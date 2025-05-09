from django.shortcuts import render

def home(request):
    """
    Vista que sirve la plantilla 'home.html'.
    """
    return render(request, 'home.html')