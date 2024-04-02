from rest_framework import serializers
from .models import CustomUser, EndUser, AdminUser
from rest_framework.authentication import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login

# User Registration serializer
class EndUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    #save end user data    
    def save(self, **kwargs):
        user = CustomUser(
            email = self.validated_data['email'], 
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.is_enduser = True
        # Save end user data to the EndUser table
        user.save()
        EndUser.objects.create(
            user = user,
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name']
        )

#Admin user registration serializer
class AdminUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    #save admin user data    
    def save(self, **kwargs):
        user = CustomUser(
            email = self.validated_data['email'], 
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.is_admin = True
        # Save end user data to the EndUser table
        user.save()
        AdminUser.objects.create(
            user = user,
        )
        
# Serializer for user login        
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'access', 'refresh']
        
    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        print(user)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, user)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
            }

            return validation
        except:
            raise serializers.ValidationError("Invalid login credentials")