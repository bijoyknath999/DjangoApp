import email
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from yaml import serialize
from . models import namaz_time_table
from . serializer import namazSerializers, UserSerializer, RegisterSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from django.views.decorators.csrf import ensure_csrf_cookie
from .tokengenerator import generate_access_token, generate_refresh_token
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



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


    # def post(self, request, *args, **kwargs):
    #     namaz_list = request.data
    #     namaz_item = namaz_time_table.objects.create(namaz_name=namaz_list["namaz_name"],
    #     namaz_time=namaz_list["namaz_time"])
    #     namaz_item.save()
    #     serializer = namazSerializers(namaz_item)
    #     return Response(serializer.data)



class UserInfo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "first_name": user.first_name,
            "last_name": user.last_name,
            'email': user.email,
            'admin_access':user.admin_access,
    })


class RegisterView(generics.CreateAPIView):
    def post(self, request):
        post_data = request.data

        serializer = RegisterSerializer(data=post_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={'user':serializer.data})
        return Response(data={'user':serializer.errors})


class LoginUser(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            serializer = self.serializer_class(user)
            token = generate_access_token(email)
            return Response({'user':serializer.data, 'token':token}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)




class CheckAdmin(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({'admin_access': user.admin_access})

# Create your views here.

