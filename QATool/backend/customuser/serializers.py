from rest_framework import serializers
from .models import Customuser

class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ('user','password', 'firstname', 'lastname', 'email','role','countrycode','phone')