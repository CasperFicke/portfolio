# blog/admin.py

# django
from django.contrib import admin

# local
from .models import (Blog)

# Register blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ('id','name','is_active')
  readonly_fields = ('slug',)
