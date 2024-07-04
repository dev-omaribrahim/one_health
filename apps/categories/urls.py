from django.urls import path
from . import views


app_name = 'categories'


urlpatterns = [
    path('', views.CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),
]