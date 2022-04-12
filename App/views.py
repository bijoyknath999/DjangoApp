from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import namaz_time_table
from . serializer import namazSerializers

class NamazList(APIView):
    def get(self, request):
        namazlist = namaz_time_table.objects.all()
        serializer = namazSerializers(namazlist, many=True)
        return Response(serializer.data)


    def post(self, request):
        pass


# Create your views here.

