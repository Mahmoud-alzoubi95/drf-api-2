from rest_framework import serializers
from .models import Glass

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glass
        fields = ('id','Name','Discription','Admine')

