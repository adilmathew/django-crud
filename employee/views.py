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
'''@api_view(['GET', 'POST'])
def employee_list(request):
    """
    
    """
    if request.method == 'GET':
        employees = Data_employ.objects.all()
        serializer = Data_employSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Data_employSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''

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


'''@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        employee = Data_employ.objects.get(pk=pk)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Data_employSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Data_employSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

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


'''@api_view([ 'POST','GET'])
def create_employ(request):
    if request.method == 'POST':
        serializer = Data_employSerializer(data=request.data)
        user=User.objects.create_user(request.POST['employee_name'], request.POST['employee_email'], request.POST['password'])
        user.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    form=form_employ
    #form2=employprofileform()
    return render(request, 'create.html', {'form': form})

'''

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
        
'''class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
'''