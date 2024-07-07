from django.urls import path
from .views import RegisterView, MyTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'users_auth'


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
