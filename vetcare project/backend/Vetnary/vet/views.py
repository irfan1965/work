from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Details, Animal
from .serializer import AnimalSerializer, DetailsSerializer, ReqSerializer, RequestUpdateSerializer, PaySearchSerializer
import random
from django.db.models import Q
import pandas as pd
from authentication.models import CustomUser


class Registration(APIView):

    def post(self, request):
        print(request.data)
        if request.data['role'] == 'animal':
            data = AnimalSerializer(data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class Request(APIView):
    def put(self, request):
        print(type(request.data))
        o = list("spXjgs51458623Xxxdd")
        random.shuffle(o)
        request.data['payment_id'] = ''.join(o)
        print(request.data)
        request.data['animal_id'] = (Animal.objects.last()).animal_id
        print(request.data)
        data = RequestUpdateSerializer(data=request.data)
        if data.is_valid():
            Data = list(Details.objects.values_list('payment_id', flat=True))
            if request.data['payment_id'] not in Data:
                data.save()

        return Response("success", status=status.HTTP_400_BAD_REQUEST)


class DoctorReceive(APIView):
    def post(self, request):
        print(request.data['email'])
        details = list(
            Details.objects.filter(doctor_email=request.data['email'], details_prescription=None).values_list(
                'animal_id', flat=True))
        animal = Animal.objects.filter(animal_id__in=details)
        req = ReqSerializer(animal, many=True)
        return Response(req.data)


class DoctorUpdate(APIView):
    def post(self, request):
        data1 = request.data.get('data')

        Details.objects.filter(animal_id=data1.get('animal_id')).update(
            details_prescription=request.data.get("details_prescription"))
        return Response("success")


class CustomerHistory(APIView):
    def post(self, request):
        custData = Details.objects.filter(customer_email=request.data['customer_email'])
        req = DetailsSerializer(custData, many=True)
        return Response(req.data)


class DoctorHistory(APIView):
    def post(self, request):
        custData = Details.objects.filter(doctor_email=request.data['doctor_email'], details_prescription__contains='')
        request = DetailsSerializer(custData, many=True)
        return Response(request.data)
        return Response("sucess")


class DetailsPayment(APIView):
    def post(self, request):
        details = Details.objects.all()
        info = RequestUpdateSerializer(details, many=True)
        return Response(info.data)


class PaySearch(APIView):
    def post(self, request):
        info = Details.objects.all().filter(
            Q(payment_id=request.data.get('payment_id')) | Q(details_prescription=request.data.get('payment_id'))
            | Q(customer_email=request.data.get('payment_id')) | Q(doctor_email=request.data.get('payment_id')) |
            Q(animal_id=request.data.get('payment_id')))

        req = PaySearchSerializer(info, many=True)
        return Response(req.data)


class pie(APIView):
    def post(self, request):
        print(request.data)

        info = Details.objects.filter(customer_email=request.data.get('email')).values_list('payment_id',
                                                                                            'details_prescription',
                                                                                            'doctor_email', 'animal_id')

        doctorcount = list(Details.objects.filter(customer_email=request.data.get('email')).values_list('doctor_email'))
        print((set(doctorcount)))
        doctorcount=set(doctorcount)
        print(len(doctorcount))
        pendingprescription = Details.objects.filter(customer_email=request.data.get('email'),details_prescription=None)
        # print(len(pendingprescription))

        paymentcount = prescriptioncount = 0
        for i in info:
            if i[0] != None:
                paymentcount += 1
        for i in info:
            if i[1] != None:
                prescriptioncount += 1
        data = [paymentcount, prescriptioncount, len(pendingprescription), len(doctorcount)]
        return Response(data)


class DoctorPie(APIView):
    def post(self, request):
        info = Details.objects.filter(doctor_email=request.data.get('email')).values_list('payment_id')
        prescription = Details.objects.filter(doctor_email=request.data.get('email')).exclude(
            details_prescription=None).values_list('details_prescription')
        noPrescription = Details.objects.filter(doctor_email=request.data.get('email'),
                                                details_prescription=None).values_list('details_prescription')
        print(len(info), len(noPrescription), len(prescription))
        l = [len(info), len(noPrescription), len(prescription)]
        print(l)
        return Response(l)


class AdminChart(APIView):
    def post(self, request):
        customer = CustomUser.objects.filter(role='customer')

        details = Details.objects.all()
        doctor = CustomUser.objects.filter(role='doctor')
        count = [len(details), len(doctor), len(customer)]
        print(count)
        return Response(count)


@permission_classes([])
@authentication_classes([])
class Practice(APIView):
    def get(self, request):
        details= CustomUser.objects.filter(email__startswith="b").values_list('email')
        print(connection.queries,"sw")
        return Response({"details":details})
