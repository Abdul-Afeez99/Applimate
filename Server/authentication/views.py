from rest_framework import generics, permissions, response, status
from .serializers import EndUserRegistrationSerializer, AdminUserRegistrationSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# user registration view
class EndUserRegistrationView(generics.CreateAPIView):
    serializer_class = EndUserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(
        operation_description="Register a new user",
        responses={status.HTTP_201_CREATED: openapi.Response("User details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email address of the user"),
                "first_name": openapi.Schema(type=openapi.TYPE_STRING, description="User first name"),
                "last_name": openapi.Schema(type=openapi.TYPE_STRING, description="User last name"),
            }
        ))}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
# Admin user registration view
class AdminRegistrationView(generics.CreateAPIView):
    serializer_class = AdminUserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(
        operation_description="Register a new admin user",
        responses={status.HTTP_201_CREATED: openapi.Response("Admin details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email address of the admin user"),
            }
        ))}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    
# login view
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    @swagger_auto_schema(
        operation_description="User login",
        responses={status.HTTP_201_CREATED: openapi.Response("login details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email address of the user"),
                "access": openapi.Schema(type=openapi.TYPE_STRING, description="Access token"),
                "refresh": openapi.Schema(type=openapi.TYPE_STRING, description="Refresh token"),
            }
        ))}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)