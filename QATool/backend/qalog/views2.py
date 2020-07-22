from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import QALogSerializer      # add this
from .models import QALog                     # add this
from django_filters.rest_framework import DjangoFilterBackend    

class QALogView(viewsets.ModelViewSet):       # add this
    serializer_class = QALogSerializer          # add this
    queryset = QALog.objects.all()
# Create your views here.
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['SystemType', 'QAConnID']