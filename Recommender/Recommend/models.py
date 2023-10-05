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
class Counter(models.Model):
    Tag_Name = models.CharField(max_length=100,null=True)
    Pupil = models.IntegerField()
    Specialist = models.IntegerField()
    Expert = models.IntegerField()
    Candidate_Master = models.IntegerField()
    Master = models.IntegerField()

class Handle(models.Model):
    handle= models.CharField(max_length=100,null=False,primary_key=True)