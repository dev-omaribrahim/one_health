from django.urls import path
from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.PostListCreateAPIView.as_view(), name='post_list_create'),
    path('<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail'),
    path('<int:post_id>/comments/', views.CommentListCreateAPIView.as_view(), name='comment_list_create'),
    path('<int:post_id>/comments/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment_detail'),
]