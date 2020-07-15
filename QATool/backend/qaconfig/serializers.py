from rest_framework import serializers
from .models import Qaconfig

class QaconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qaconfig
        fields = ('id','qaconnid', 'systemtype', 'ipaddress', 'port', 'adminuser', 'adminpass', 'sysid', 'client', 'githuburl', 'triggerrate', 'triggeruom')