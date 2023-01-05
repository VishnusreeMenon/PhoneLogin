from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('patient/',views.PatientEventApi.as_view(),name = 'patientEvent'),
    path('doctor/',views.DoctorEventApi.as_view(),name = 'doctorEvent'),
    
]