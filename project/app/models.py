from django.db import models

# Create your models here.
class Careers(models.Model):
    # this is not career model ,its a searchvenues model
    name=models.CharField(max_length = 200)
    titles=models.CharField(max_length = 200)
class Applyform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=13)
    position=models.CharField(max_length=50)
    experience=models.IntegerField()
    cover_letter=models.CharField(max_length=150)
    resume=models.FileField(upload_to="Files")
