from django.urls import path
from decision_engine.views import Create_Decision_View,Specific_Decision_View,List_Decisions_View


urlpatterns = [
    path('createdecision/',Create_Decision_View.as_view(),name='create_decision'),
    path('decision/<int:did>',Specific_Decision_View.as_view(),name='specific_decision'),
    path('decisions/',List_Decisions_View.as_view(),name='list_decisions'), 
]