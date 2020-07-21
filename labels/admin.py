from django.contrib import admin

# Register your models here.
from labels.models import Labels

admin.site.register(Labels, admin.ModelAdmin)