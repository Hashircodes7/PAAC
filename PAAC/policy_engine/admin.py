from django.contrib import admin
from policy_engine.models import Policy

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'policy_name', 'action', 'resource_type', 'effect', 
        'priority', 'is_active', 'created_by', 'updated_by', 'created_at', 'updated_at'
    ]
    search_fields = ['policy_name', 'action', 'resource_type', 'effect', 'created_by__username', 'updated_by__username']
    list_filter = ['action', 'resource_type', 'effect', 'is_active', 'priority', 'created_at', 'updated_at']
