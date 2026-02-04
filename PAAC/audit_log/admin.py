# audit_log/admin.py
from django.contrib import admin
from audit_log.models import Audit

@admin.register(Audit)
class Audit_Admin(admin.ModelAdmin):
    list_display = ['id', 'decision', 'audit_time']
    search_fields = ['decision__user__username', 'decision__policy_used__policy_name', 'decision__result']
    list_filter = ['audit_time', 'decision__result']
