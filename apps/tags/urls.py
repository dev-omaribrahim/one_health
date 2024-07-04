from django.urls import path
from . import views


app_name = 'tags'


urlpatterns = [
    path('', views.TagListCreateAPIView.as_view(), name='tag_list_create'),
    path('<int:pk>/', views.TagRetrieveUpdateDestroyAPIView.as_view(), name='tag_detail'),
]