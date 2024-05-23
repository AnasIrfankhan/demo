# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import AbstractUser, PermissionsMixin

# class CustomUser(AbstractUser, PermissionsMixin):
#     first_name = models.CharField(max_length=100, null=False)
#     middle_name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, null=False)
#     password=models.CharField(max_length=100, null=False)
#     email = models.EmailField(unique=True, null=False)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
    
#     # Define the role relationship
#     role = models.ManyToManyField('models.role', blank=True, related_name='user')

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth import authenticate
# from .models import CustomUser

# class CustomAuthToken(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def post(self, request, *args, **kwargs):
#         email = request.data.get("email")
#         password = request.data.get("password")
#         user = authenticate(email=email, password=password)

#         if user:
#             jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#             jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#             payload = jwt_payload_handler(user)
        #     token = jwt_encode_handler(payload)
        #     return Response({'token': token, 'role': user.role})
        # else:
        #     return Response({'error': 'Invalid credentials'}, status=400)
