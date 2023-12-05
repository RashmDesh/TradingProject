from django.db import models

# Create your models here.
class treadingfile(models.Model):
    file=models.FileField(upload_to='uploadedfiles/',default="")
    upload_time = models.DateTimeField(auto_now_add=True)
