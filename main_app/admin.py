from django.contrib import admin

# Register your models here.
from .models import Stone, Use

# Register your models here
admin.site.register(Stone)
admin.site.register(Use)