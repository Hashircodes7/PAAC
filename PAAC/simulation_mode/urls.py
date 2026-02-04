from django.urls import path
from simulation_mode.views import  Simulate_Decision_View,List_Simulation_View,Specific_Simulation_View

urlpatterns = [
    path('simulatedecision/',Simulate_Decision_View.as_view(),name='simulate_decision'),
    path('simulations/',List_Simulation_View.as_view(),name='list_simulations'),
    path('simulations/<int:sid>/',Specific_Simulation_View.as_view(),name='specific_simulation'), 
]