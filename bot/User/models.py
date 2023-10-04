from django.db import models

# Create your models here.
class Contastant(models.Model):

    c_id = models.IntegerField()
    c_name = models.CharField(max_length=40)
    c_email = models.EmailField(max_length=30)


class Handle_Name(models.Model):
    Name=models.CharField(max_length=40)
