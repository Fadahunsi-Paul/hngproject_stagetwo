from rest_framework import serializers
from .models import *

#creating serializer class
class PersonSerializer(serializers.ModelSerializer):
    #importing the model fields to be used 
    class Meta:
        model = Person
        fields = '__all__'


        