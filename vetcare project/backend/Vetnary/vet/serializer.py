from rest_framework import serializers

from .models import Details, Animal


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['animal_name', 'animal_image', 'animal_symptom', 'animal_amount', 'animal_age', 'animal_loc',
                  'customer_email']


class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['animal_name', 'animal_image', 'animal_symptom', 'animal_age', 'animal_amount', 'animal_loc',
                  'customer_email', 'animal_id']


class RequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['payment_id', 'customer_email', 'doctor_email', 'animal_id']


class PaySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'
