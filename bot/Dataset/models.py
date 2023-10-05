from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Handle(models.Model):
    handle = models.CharField(max_length=40,primary_key=True)