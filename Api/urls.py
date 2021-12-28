from django.urls import path
from django.conf.urls import include
from.views import RegisterView, UserDetails, UsersLists
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

   path('register/',RegisterView.as_view(),name='register'),
   
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('UsersLists/',UsersLists.as_view(),name="UsersLists"),
   path('userDetails/<int:pk>/',UserDetails.as_view(),name="userDetails"),
]
