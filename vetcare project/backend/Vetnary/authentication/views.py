from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from threading import Timer
from rest_framework import status, request, serializers
from .serializer import DoctorSerializer, CustomerSerializer, userDoctorSerializer, userCustomerSerializer, \
    AdminLoginSerialization
from .models import CustomUser
from django.core import serializers
from django.db.models import Q
import jwt, datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
import datetime



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@permission_classes([])
@authentication_classes([])
class Login(APIView):

    def post(self, request):
        print(request.data)
        details = CustomUser.objects.filter(email=request.data["email"]).first()

        print(details)
        if details is None:
            # return Response('enter valid email')
            raise AuthenticationFailed('User Not Found')

        if not details.check_password(request.data["password"]):
            # return Response('enter valid password')
            raise AuthenticationFailed('wrong password')

        # if (request.data['email'], request.data['password']) in list(details):
        # def get(self, request):
        # print(details[0].role)
        # payload = {
        #     'id': details.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=20),
        #     'iat': datetime.datetime.utcnow()
        # }
        # print(payload['exp'],"kihj")
        # token = jwt.encode(payload, 'secret', algorithm='HS256')
        # refresh = RefreshToken.for_user(details)

        refresh = MyTokenObtainPairSerializer.get_token(details)

        if details.role == "doctor":
            js = DoctorSerializer(details)
            response = {'token': str(refresh.access_token), 'refresh_token': str(refresh)}
            response.update(js.data)
            return Response(response)

        elif details.role == "customer":
            js = CustomerSerializer(details)
            response = {'token': str(refresh.access_token), 'refresh_token': str(refresh)}
            response.update(js.data)
            return Response(response)
        elif details.role == 'admin':
            print(details, "hj")
            js = AdminLoginSerialization(details)

            response = {'token': str(refresh.access_token), 'refresh_token': str(refresh)}
            response.update(js.data)
            return Response(response)
        else:
            return Response("Invalid credentials", status=status.HTTP_200_OK)


@permission_classes([])
@authentication_classes([])
class Register(APIView):

    def post(self, request):
        if request.data['email'] not in CustomUser.objects.values_list('email', flat=True):
            if request.data['role'] == 'doctor':
                data = DoctorSerializer(data=request.data)
            else:
                data = CustomerSerializer(data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data, status=status.HTTP_201_CREATED)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("already exists", status=status.HTTP_201_CREATED)


class DocInfo(APIView):
    def post(self, request):
        details = CustomUser.objects.filter(role='doctor')
        js = DoctorSerializer(details, many=True)
        return Response(js.data)


class Details(APIView):
    def post(self, request):
        userDetails = CustomUser.objects().all()
        js = CustomerSerializer(userDetails, many=True)
        return (js)


class DetailsCustomer(APIView):
    def post(self, request):
        userDetails = CustomUser.objects().all()
        js = userCustomerSerializer(userDetails, many=True)
        return (js)


class DetailPaymentSerializer(APIView):
    def post(self, request):
        userDetails = CustomUser.objects().all()
        js = userCustomerSerializer(userDetails, many=True)
        return (js)


class AdminUserDetails(APIView):
    def post(self, request):
        req = CustomUser.objects.filter(role='customer')
        js = CustomerSerializer(req, many=True)
        return Response(js.data)


class AdminUserSearch(APIView):
    def post(self, request):
        req = CustomUser.objects.filter(Q(role='customer') & Q(email=request.data.get('search')) |
                                        Q(location=request.data.get('search')) |
                                        Q(mobile_number=request.data.get('search')))
        js = CustomerSerializer(req, many=True)
        return Response(js.data)


class AdminDoctorSearch(APIView):
    def post(self, request):
        req = CustomUser.objects.filter(Q(role='doctor') & Q(email=request.data.get('search')) |
                                        Q(location=request.data.get('search')) |
                                        Q(mobile_number=request.data.get('search')))
        js = CustomerSerializer(req, many=True)
        return Response(js.data)
