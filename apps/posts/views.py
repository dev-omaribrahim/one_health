from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs['post_id'])
        serializer.save(post=post)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

