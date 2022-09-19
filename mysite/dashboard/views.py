from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import load
from .serializers import DashboardSerializers


def dashboard(request):
    return render(request, 'dashboard/index.html')


class api_table(ModelViewSet):
    queryset = load.objects.all()
    serializer_class = DashboardSerializers
