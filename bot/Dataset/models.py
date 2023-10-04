from django.db import models

# Create your models here.
class CM_to_Master(models.Model):
    p_id = models.IntegerField()
    index= models.CharField(max_length=1)
    name = models.CharField(max_length=30)
    rating = models.IntegerField()

