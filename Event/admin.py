from django.contrib import admin
from .models import PatientEvent,DoctorEvent
# Register your models here.
admin.site.register(PatientEvent)
admin.site.register(DoctorEvent)