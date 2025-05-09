from django.contrib import admin
from .models import Stream

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ('provider_name', 'category', 'is_live')
    list_filter = ('category', 'is_live')
    search_fields = ('provider_name',)