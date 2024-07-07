from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or Tag.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            self.slug = slugify(self.name)
            counter = 1
            while Tag.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{slugify(self.name)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name