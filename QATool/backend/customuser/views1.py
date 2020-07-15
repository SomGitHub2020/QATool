from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import CustomuserSerializer      # add this
from .models import Customuser                     # add this
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os 

class CustomuserView(viewsets.ModelViewSet):       # add this
    serializer_class = CustomuserSerializer          # add this
    queryset = Customuser.objects.all()              # add this    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'role']

class ReactAppView(View):

    def get(self, request):
        try:

            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )