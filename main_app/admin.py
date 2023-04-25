from django.contrib import admin

# Register your models here.
from .models import Stone, Use, Villain

# Register your models here
admin.site.register(Stone)
admin.site.register(Use)
admin.site.register(Villain)