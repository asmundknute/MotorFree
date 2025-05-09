from django.db import models
from categories.models import Category

class Stream(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=100)
    provider_logo = models.ImageField(upload_to='streaming/logos/')
    stream_url = models.URLField()
    is_live = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.provider_name} - {self.category.name}"