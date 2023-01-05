from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Account.models import NewUser,Profile
from .models import PatientEvent,DoctorEvent
from .serializer import PatientEventSerialser,DoctorEventSerialser
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
# Create your views here.


class PatientEventApi(APIView):
    
    def post(self, request):
        data = request.data
        data['patient'] = request.user.username
        serializer = PatientEventSerialser(data = data)
        try:

            if serializer.is_valid():
                
                try:
                    doc = User.objects.get(username = serializer.validated_data['doctor'])
                    doc = NewUser.objects.get(user = doc)
                    doc = Profile.objects.get(person = doc)
                    
                    # print(tuple(data.values()))
                    topic,doctor,start_time,end_time,patient,meet_link = data.values()
    
                    if doc.role.lower() == 'doctor':
                        if PatientEvent.objects.filter(topic = topic,doctor = doctor,start_time = start_time,end_time = end_time).exists():\
                            return Response({
                            'status':400,
                            'message':"Appointment already exists!",
                            'data' : serializer.errors
                            })
                        serializer.save()
                        return Response(
                            {
                                'status':200,
                                'message':'Appointment created',
                                'data':serializer.data
                            }
                        )
                    else:
                        return Response({
                        'status':400,
                        'message':"Doctor does not exist",
                        'data' : serializer.errors
                        })
                           
                except Exception as e:
                    print("test -",e)
                    return Response({
                    'status':400,
                    'message':"User does not exist",
                    'data' : serializer.errors
                    })                     
                    
            return Response({
                'status':400,
                'message':"There was some error",
                'data' : serializer.errors
            })

        except Exception as e:
            print("error viwes-",e)
            


class DoctorEventApi(APIView):
    
    def post(self, request):
        data = request.data
        data['doctor'] = request.user.username
        serializer = DoctorEventSerialser(data = data)
        try:

            if serializer.is_valid():
                print()
                try:
                    pat = User.objects.get(username = serializer.validated_data['patient'])
                    pat = NewUser.objects.get(user = pat)
                    pat = Profile.objects.get(person = pat)
                    topic,patient,start_time,end_time,doctor,meet_link = data.values()
                    if pat.role.lower() == 'patient':
                        if DoctorEvent.objects.filter(topic = topic,patient = patient,start_time = start_time,end_time = end_time).exists():
                            return Response({
                            'status':400,
                            'message':"Appointment already exists!",
                            'data' : serializer.errors
                            })
                        serializer.save()
                        
                        return Response(
                            {
                                'status':200,
                                'message':'Appointment created',
                                'data':serializer.data
                            }
                        )
                        
                    else:
                        return Response({
                        'status':400,
                        'message':"Patient does not exist",
                        'data' : serializer.errors
                        })
                           
                except Exception as e:
                    print("test -",e)
                    return Response({
                    'status':400,
                    'message':"User does not exist",
                    'data' : serializer.errors
                    })                     
                    
            return Response({
                'status':400,
                'message':"There was some error",
                'data' : serializer.errors
            })

        except Exception as e:
            print("error viwes-",e)
            
        