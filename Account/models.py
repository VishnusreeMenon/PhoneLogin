from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid
from django.contrib.auth import get_user_model

class NewUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=6,null=True,blank=True)
    phone_number = models.CharField(max_length=14)
    uid = models.UUIDField(default=uuid.uuid4())
    
    def __str__(self):
        return self.user.username    


class Profile(models.Model):
    
    person  = models.ForeignKey(NewUser,on_delete=models.DO_NOTHING)
    profile_score = models.IntegerField()
    mental_score = models.IntegerField()
    role = models.CharField(max_length=255,blank=False)
    
    def __str__(self):
        return self.person.phone_number