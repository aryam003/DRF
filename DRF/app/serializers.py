from rest_framework import serializers
from . models import *
class sample(serializers.Serializer):
    Name=serializers.CharField()
    Age=serializers.IntegerField()
    Email=serializers.EmailField()
    Place=serializers.CharField()

class model_serializer(serializers.ModelSerializer):
    class Meta:
        model=project_user
        fields='__all__'

