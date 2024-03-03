from django.db import models

# Create your models here.
class AutherModel(models.Model):
   aname=models.CharField(max_length=10)
   nump=models.IntegerField()
   amobile=models.IntegerField()
   aemail=models.EmailField()

