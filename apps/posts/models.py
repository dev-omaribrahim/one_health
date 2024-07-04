from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        'profiles.Profile', 
        related_name='posts', 
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        'categories.Category', 
        related_name='posts'
    )
    tags = models.ManyToManyField(
        'tags.Tag', 
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
    def __str__(self):
        return f'Comment by {self.author.user.username} on {self.post.title}'