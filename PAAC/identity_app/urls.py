from django.urls import path
from identity_app.views import Create_User_View,Update_User_View,Delete_User_View,Get_Spec_User,Get_Users
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('createuser/',Create_User_View.as_view(),name='create_user'),
    path('updateuser/<int:uid>',Update_User_View.as_view(),name='update_user'),
    path('deleteuser/<int:uid>',Delete_User_View.as_view(),name='delete_user'),
    path('allusers/',Get_Users.as_view(),name='all_users'),
    path('user/<int:uid>',Get_Spec_User.as_view(),name='spec_user'),

]