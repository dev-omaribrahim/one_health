from django.urls import path
from . import views


app_name = 'profiles'


urlpatterns = [
    path('', views.ProfileListCreateAPIView.as_view(), name='profile_list_reate'),
    path('<int:pk>/', views.ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile_detail'),
]