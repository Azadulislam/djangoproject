from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank="true", max_length=254, unique=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=700)

    def __str__(self):
        return self.subject
