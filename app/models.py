from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="media/images/")
    ratings=models.IntegerField(default=0)
    message=models.CharField(max_length=5000)