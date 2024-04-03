from rest_framework import serializers
from .models import ApplicantDetails, ApplicationDetails
from authentication.models import CustomUser

# Applicant details serializer
class ApplicantDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantDetails
        fields = ['resume_link', 'portfolio_link']
        
        
        
# Application details serializer
class ApplicationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDetails
        fields = ['pk', 'position', 'status', 'application_date', 'job_link', 'location']
        extra_kwargs = {
            'pk': {'read_only': True}
        }
    
    
