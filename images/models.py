from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
