from rest_framework import serializers
from . models import namaz_time_table
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class namazSerializers(serializers.ModelSerializer):
    class Meta:
        model = namaz_time_table
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    User = get_user_model()
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        User = get_user_model()
        model = User
        fields = ('email', 'password', 'first_name', 'last_name','admin_access')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password']),
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        )
        return user



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        User = get_user_model()
        model = User
        fields =('id', 'email',
                  'first_name', 'last_name','password', 'admin_access')

