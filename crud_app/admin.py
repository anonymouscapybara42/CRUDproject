from django.contrib import admin
from .models import Item  # Changed back to Item

admin.site.register(Item)