from django.db import models


class UserPlayList(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    videos_qty = models.IntegerField(default=0)
    views_qty = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
