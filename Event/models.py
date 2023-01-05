from django.db import models

# Create your models here.

class PatientEvent(models.Model):
    patient = models.CharField(max_length=255,blank=True)
    doctor = models.CharField(max_length=255,blank=False)
    topic = models.CharField(max_length=255,blank=False)
    start_time = models.DateTimeField(max_length=255,blank=False)
    end_time = models.DateTimeField(max_length=255,blank=False)
    meet_link = models.CharField(max_length=12,blank=True)
    
    def __str__(self):
        return self.topic
    
    
class DoctorEvent(models.Model):
    doctor = models.CharField(max_length=255,blank=True)
    patient = models.CharField(max_length=255,blank=False)
    topic = models.CharField(max_length=255,blank=False)
    start_time = models.DateTimeField(max_length=255,blank=False)
    end_time = models.DateTimeField(max_length=255,blank=False)
    meet_link = models.CharField(max_length=12,blank=True)
    def __str__(self):
        return self.topic