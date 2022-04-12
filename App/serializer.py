from rest_framework import serializers
from . models import namaz_time_table

class namazSerializers(serializers.ModelSerializer):
    class Meta:
        model = namaz_time_table
        fields = '__all__'

