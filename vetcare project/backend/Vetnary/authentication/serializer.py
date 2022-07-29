from rest_framework import serializers
from .models import CustomUser


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'email', 'role', 'location', 'doctor_exp', 'mobile_number', 'doctor_image',
                  'timeslot', 'doctor_designation', 'password']
        extra_kwards = {
            'password': {'write_only': True}

        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'role', 'location', 'mobile_number', 'password', 'id', 'first_name']

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class userDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class userCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'firstname', 'mobile_number', 'location', 'role']


class AdminLoginSerialization(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'role']
