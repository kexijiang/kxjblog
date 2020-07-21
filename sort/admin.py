from django.contrib import admin

# Register your models here.
from sort.models import Sort

admin.site.register(Sort, admin.ModelAdmin)