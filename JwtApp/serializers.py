from .models import Student,User,role
from rest_framework import serializers


class Student_serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class UserView_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        
class role_serializers(serializers.ModelSerializer):
    class Meta:
        model=role
        fields='__all__'


class User_Serializers(serializers.ModelSerializer):

    # roles=role_serializers(many=True,read_only=True)


    class Meta:
        model=User
        # fields=['id', 'username','first_name','middle_name','last_name','password', 'email', ] 
        fields='__all__' 
        depth = 1


class Login_serializers(serializers.Serializer):

    email=serializers.EmailField()
    password=serializers.CharField(max_length=100)
    role =serializers.CharField(max_length=60)


class changed_password_serializers(serializers.Serializer):
    current_password= serializers.CharField(max_length=30)
    change_password=serializers.CharField(max_length=30)
    email =serializers.EmailField()

class forgot_password_serializers(serializers.Serializer):
    # old_password=serializers.CharField(max_length=30)
    new_password = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    otp=serializers.CharField(max_length=50)
    
# ------------------------------------------------------------

from .models import Employer, Manager
class Emp_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields='__all__'


class Manager_Serializers(serializers.ModelSerializer):
    class Meta :
        model = Manager
        fields='__all__'


class Reset_PasswordSerializer(serializers.Serializer):
    email=serializers.EmailField()


class  Forgot_Password_Serializer(serializers.Serializer):
    email = serializers.EmailField()
    otp=serializers.CharField(max_length = 6)
    new_password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)


    def validate(self,data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data




# ----------------------------------- chat gpt


# from rest_framework import serializers
# from .models import Student, User

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     role = serializers.PrimaryKeyRelatedField(queryset=role.objects.all())  # for POST requests

#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name', 'role']

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         if self.context['request'].method == 'GET':  # Check request method
#             role_name = instance.role.name
#             data['role'] = role_name
#         return data



# # 