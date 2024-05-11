from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(null=False, max_length=50)
    description = models.TextField(null=False)