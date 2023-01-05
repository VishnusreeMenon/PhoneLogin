from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import DoctorEvent,PatientEvent


class PatientEventSerialser(serializers.ModelSerializer):
    
    class Meta:
        model = PatientEvent
        fields = '__all__'
        

class DoctorEventSerialser(serializers.ModelSerializer):
    
    class Meta:
        model = DoctorEvent
        fields = '__all__'
        