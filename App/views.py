from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . models import namaz_time_table
from . serializer import namazSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication


# @api_view(['GET' , 'POST'])
# def NamazListView(request):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     if request.method == 'GET':
#         namazlist = namaz_time_table.objects.all()
#         nserializer = namazSerializers(namazlist , many=True)
#         return Response(nserializer.data)

#     elif request.method == 'POST':
#         nserializer = namazSerializers(data = request.data)
#         if nserializer.is_valid():
#             nserializer.save()
#             return Response(nserializer.data , status=status.HTTP_201_CREATED)
        
#         return Response(nserializer.errors)

class NamazList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        namazlist = namaz_time_table.objects.all()
        serializer = namazSerializers(namazlist, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        namaz_list = request.data
        namaz_item = namaz_time_table.objects.create(namaz_name=namaz_list["namaz_name"],
        namaz_time=namaz_list["namaz_time"])
        namaz_item.save()
        serializer = namazSerializers(namaz_item)
        return Response(serializer.data)


# Create your views here.

