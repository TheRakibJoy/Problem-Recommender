from django.db import models

# Create your models here.
class Pupil(models.Model):
    PID = models.IntegerField()
    Index = models.CharField(max_length=3)
    Rating = models.IntegerField(null=True)
    Tags = models.CharField(max_length=600,null=True)

class Specialist(models.Model):
    PID = models.IntegerField()
    Index = models.CharField(max_length=3)
    Rating = models.IntegerField(null=True)
    Tags = models.CharField(max_length=600,null=True)

class Expert(models.Model):
    PID = models.IntegerField()
    Index = models.CharField(max_length=3)
    Rating = models.IntegerField(null=True)
    Tags = models.CharField(max_length=600,null=True)

class Candidate_Master(models.Model):
    PID = models.IntegerField()
    Index = models.CharField(max_length=3)
    Rating = models.IntegerField(null=True)
    Tags = models.CharField(max_length=600,null=True)

class Master(models.Model):
    PID = models.IntegerField()
    Index = models.CharField(max_length=3)
    Rating = models.IntegerField(null=True)
    Tags = models.CharField(max_length=600,null=True)
