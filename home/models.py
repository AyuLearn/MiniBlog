from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=900)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    slug = models.CharField(max_length=800)
    content = models.TextField()

    def __str__(self):
        return self.title