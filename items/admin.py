from django.contrib import admin
from .models import GroceryItems
from .models import Store

# Register your models here.
admin.site.register(GroceryItems)
admin.site.register(Store)
