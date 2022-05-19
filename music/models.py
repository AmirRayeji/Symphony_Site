from django.db import models


class Music(models.Model):
    name=models.CharField(max_length=100)
    singer=models.CharField(max_length=100)
    biography=models.TextField()
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
    image=models.ImageField()

    def __str__(self):
        return self.text


class Profile(models.Model):
    fullname=models.CharField(max_length=50)
    man=1
    woman=2
    status_choices=(('man', 'مرد'),('woman', 'زن'))
    gender=models.IntegerField(choices=status_choices)
    progile=models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.fullname
