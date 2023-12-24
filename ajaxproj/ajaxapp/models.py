from django.db import models

# Create your models here.
class FileData(models.Model):
    title = models.CharField('Title',max_length=100)
    flename = models.FileField('filename',upload_to='media/')