from django.db import models

# Create your models here.
class Video(models.Model):
    file_path = models.FileField(upload_to="video/") # путь к видео файлу
    name = models.CharField(max_length=60) # varchar
    likes = models.IntegerField(default=0) # int
    description = models.TextField(null=True) # text # blank = False
    is_published = models.BooleanField(default=True) # boolean 

    def __str__(self):
        return self.name
    