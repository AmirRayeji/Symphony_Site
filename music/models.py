from django.db import models


class Music(models.Model):
    name=models.CharField(max_length=100)
    singer=models.CharField(max_length=100)
    biography=models.TextField()
    music=models.FileField(upload_to='music/', null=True)
    poster=models.ImageField(upload_to='poster/')

    def __str__(self):
        return self.singer


class About(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    text=models.CharField(max_length=50)
    image=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.text
