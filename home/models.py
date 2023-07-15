from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='services')
 
    def __str__(self):
        return self.title
