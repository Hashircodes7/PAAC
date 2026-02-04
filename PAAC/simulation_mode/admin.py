# simulation_mode/admin.py
from django.contrib import admin
from simulation_mode.models import Simulation

@admin.register(Simulation)
class SimulationAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'user_subject', 'decision', 'simulated_at']
    search_fields = ['created_by__username', 'user_subject__username', 'decision__result']
    list_filter = ['simulated_at']
