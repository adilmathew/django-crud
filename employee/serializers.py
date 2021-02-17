
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Data_employ
User=get_user_model()
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=500, read_only=True)

    def validate(self, data):
        
        email = data.get('email')
        password = data.get('password')

        
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        
        user = authenticate(username=email, password=password)

        
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        if user.is_active:
            token=get_tokens_for_user(user)

        return {
            'email': user.email,
            'token': token,
        }



class EmployeelistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Data_employ
        fields = ['employee_name','employee_email','employee_contact',]

   
class EmployeeupdateSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=100)
    employee_name=serializers.CharField(max_length=100,required=False)
    employee_email=serializers.CharField(max_length=100,required=False)
    employee_contact=serializers.CharField(max_length=200,required=False)



    def update(self,validated_data):
        email=validated_data.get('email')
        try:
            instance=Data_employ.objects.get(employee_email=email)
        except instance.DoesNotExist:
            raise serializers.ValidationError('employee to be updated does not exist') 

        instance.employee_name=validated_data.get('employee_name',instance.employee_name)
        instance.employee_email=validated_data.get('employee_email',instance.employee_email)
        instance.employee_contact=validated_data.get('employee_contact',instance.employee_contact)
        instance.save()
        return instance        


class EmployeeSerializer(serializers.Serializer):
    user_email=serializers.CharField(max_length=100)
    employee_name=serializers.CharField(max_length=100)
    employee_email=serializers.CharField(max_length=100)
    employee_contact=serializers.CharField(max_length=200)
    

    def create(self,validated_data):
        user_email=validated_data.pop('user_email')
        print(validated_data)
        user=get_user_model().objects.get(email=user_email)
        employee= Data_employ.objects.create(user=user,**validated_data)
        #employee.save()
        validated_data['user_email']=user_email
        return validated_data
    
    def update(self,instance,validated_data):
        instance.employee_name=validated_data.get('employee_name',instance.employee_name)
        instance.employee_email=validated_data.get('employee_email',instance.employee_email)
        instance.employee_contact=validated_data.get('employee_contact',instance.employee_contact)
        instance.save()
        return validated_data
        