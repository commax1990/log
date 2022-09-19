from rest_framework.serializers import ModelSerializer

from .models import load


class DashboardSerializers(ModelSerializer):
    class Meta:
        model = load
        fields = ['id', 'itsnumber', 'driver', 'Company', 'load', 'truck', 'trailer', 'status', 'status', 'dispatcher']
