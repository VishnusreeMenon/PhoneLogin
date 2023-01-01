from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import NewUser,Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']
        
        
class NewUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        
        model = NewUser
        fields = '__all__'
        extra_kwargs = {
           "user": {'read_only': True},
        }
        # exclude = 'person_id'
    def create(self, validated_data):   #for nested fields
        # print('here')
        data = validated_data.pop('user')
        user = get_user_model().objects.create_user(**data)
        validated_data.update({'user': user})
        profile,created = NewUser.objects.update_or_create(user = validated_data.get('user'),defaults={'phone_number':validated_data.get('phone_number')} ) 
                    
        return profile
        

class ProfileSerializer(serializers.ModelSerializer):
    # test_person = NewUserSerializer(source = 'person',read_only=True)
    # person = NewUserSerializer()
    # print(person)
    class Meta:
        model = Profile
        # depth = 1
        fields = ['person','profile_score','mental_score','role']

