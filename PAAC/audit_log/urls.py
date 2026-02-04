from django.urls import path
from audit_log.views import Audit_List_View,Policy_Audit_View,User_Audit_View

urlpatterns = [
    path('all/',Audit_List_View.as_view(),name='audit_list'),
    path('policy/<int:pid>/',Policy_Audit_View.as_view(),name='policy_audit'),
    path('user/<int:uid>/',User_Audit_View.as_view(),name='user_audit'), 
]