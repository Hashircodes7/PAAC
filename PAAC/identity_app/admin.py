from django.contrib import admin
from identity_app.models import User
# Register your models here.
@admin.register(User)
class User_Register(admin.ModelAdmin):
    list_display=['id','username','age','department','role','experience','trust_score','is_active']
    search_fields=['username','department','role','experience','is_active']
    list_filter=['id','username','department','role','experience','is_active']
