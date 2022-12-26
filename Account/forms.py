from django import forms
from django.contrib.auth.models import User
from .models import Profile,NewUser

roles = [
    ('doctor','Doctor'),
    ('patient','Patient')
    
]


class ProfileForm(forms.ModelForm):
    # person = forms.ModelChoiceField(queryset=NewUser.objects.all())
    role = forms.CharField(label="Select your current role:",widget=forms.Select(choices=roles))
    mental_score = forms.IntegerField(label='Enter Mental score')
    profile_score = forms.IntegerField(label='Enter Profile score')
    
    class Meta():
        model = Profile       
        # fields = ('person','role','mental_score','profile_score')
        fields = ('role','mental_score','profile_score')