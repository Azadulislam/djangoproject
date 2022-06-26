from ckeditor.fields import RichTextField
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=500, blank=False)
    image = models.ImageField(upload_to="about/", blank=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


COLOR = (('BLUE', 'BLUE'), ("RED", 'RED'))


class Slider(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = RichTextField()
    image = models.ImageField(upload_to="slider/", blank=False)
    extra_title = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.BooleanField(blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE)
    color = models.CharField(choices=COLOR, default="BLUE", max_length=50)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=255, blank=False)
    link = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to="client/", blank=False)

    def __str__(self):
        return self.name
