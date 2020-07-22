from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import QaconfigSerializer      # add this
from .models import Qaconfig                     # add this
from django_filters.rest_framework import DjangoFilterBackend

class QaconfigView(viewsets.ModelViewSet):       # add this
    serializer_class = QaconfigSerializer          # add this
    queryset = Qaconfig.objects.all()              # add this
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['systemtype']