from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='profile_pics/Doctor/')

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    symptoms = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/Patient/')
    assignedDoctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)

class Appointment(models.Model):
    description = models.TextField()
    status = models.BooleanField(default=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
class PatientDischargeDetails(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    discharge_date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)