from rest_framework import serializers
from .models import Parameter

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['id','id_param','title','amount','updated_at']

    