from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from .models import Data_employ
from .serializers import EmployeelistSerializer,LoginSerializer,EmployeeSerializer, EmployeeupdateSerializer
from .models import Data_employ
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
#from .models import employ_Form,employprofileform
from django.views.decorators.csrf import csrf_exempt


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't  have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

class EmployeelistView(APIView):
    permissions=[permissions.IsAuthenticated]
    serializer_class=EmployeelistSerializer


    def get(self,request):
        queryset=Data_employ.objects.all()
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)




class EmployeedetailView(APIView):
    permissions=[permissions.IsAuthenticated]
    serializer_class=EmployeelistSerializer


    def get(self,request):
        email=request.data.get('employee_email')
        try:
            query =  Data_employ.objects.get(employee_email=email)
        except query.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(query)
        return Response(serializer.data)




class EmployeecreateView(APIView):
    permissions=[permissions.IsAuthenticated]
    serializer_class=EmployeeSerializer


    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class EmployeeupdateView(APIView):
    permissions=[permissions.IsAuthenticated]
    serializer_class=EmployeeupdateSerializer


    def put(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        serializer.is_valid()
        serializer.update(data)
        
        return Response(serializer.data)
        
