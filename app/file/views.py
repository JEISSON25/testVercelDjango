from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class FileViewset(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer
