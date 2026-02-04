# decision_engine/admin.py
from django.contrib import admin
from decision_engine.models import Decision

@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'policy_used', 'result', 'reason']
    search_fields = ['user__username', 'policy_used__policy_name', 'result']
    list_filter = ['result', 'policy_used']
