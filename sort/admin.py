from django.contrib import admin

# Register your models here.
from sort.models import Sort, Article_sort

admin.site.register(Sort, admin.ModelAdmin)

admin.site.register(Article_sort, admin.ModelAdmin)
