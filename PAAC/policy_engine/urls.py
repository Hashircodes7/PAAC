from django.urls import path
from policy_engine.views import Create_Policy_View,Update_Policy_View,Delete_Policy_View,List_Policies,Get_Spec_Policy

urlpatterns = [
    path('createpolicy/',Create_Policy_View.as_view(),name='create_policy'),
    path('updatepolicy/<int:pid>',Update_Policy_View.as_view(),name='update_policy'),
    path('deletepolicy/<int:pid>',Delete_Policy_View.as_view(),name='delete_policy'),
    path('allpolicies/',List_Policies.as_view(),name='list_policies'),
    path('policy/<int:pid>',Get_Spec_Policy.as_view(),name='get_policy'),

]