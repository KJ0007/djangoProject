from django.db import models

# Create your models here.
class PublisherModel(models.Model):
    aname=models.CharField(max_length=10)
    bname=models.CharField(max_length=10)
    bpage=models.IntegerField()
    bprice=models.FloatField()
    aemail=models.EmailField()