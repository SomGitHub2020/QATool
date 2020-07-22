from rest_framework import serializers
from .models import QALog

class QALogSerializer(serializers.ModelSerializer):
    class Meta:
        model = QALog
        fields = ('id','SystemType','QAConnID','QACreatedDate','JIRALogFlag','QALog','QALoggedDate','ObjectName','ObjectPath','DevelopedBy')