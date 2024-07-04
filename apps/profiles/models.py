from django.db import models
from apps.users_auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
    def __str__(self):
        return self.user.username
