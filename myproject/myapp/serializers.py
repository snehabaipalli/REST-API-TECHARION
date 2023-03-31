from rest_framework import serializers
from .models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

#class studentMarkSerializer(serializers.ModelSerializer):
    #class Meta:
        #model=studentMarks
        #fields='__all__'