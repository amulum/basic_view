from django.db import models

# Create your models here.
class Blog(models.Model):
    image_path      = models.CharField(max_length=300)
    header          = models.CharField(max_length=300)
    content         = models.TextField(max_length=2000)
    date            = models.CharField(max_length=30)
    comment         = models.CharField(max_length=30)
    def __str__(self):
        return self.header

class Mentor(models.Model):
    image_path      = models.CharField(max_length=300)
    name            = models.CharField(max_length=100)
    experience      = models.CharField(max_length=300)
    quote           = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Mentee(models.Model):
    image_path      = models.CharField(max_length=300)
    name            = models.CharField(max_length=100)
    quote           = models.CharField(max_length=300)
    def __str__(self):
        return self.name