from django.shortcuts import render
from .serializers import ApplicantDetailsSerializer, ApplicationDetailsSerializer
from rest_framework.views import APIView
from rest_framework import permissions, generics, response, status
from .permissions import IsUser
from .models import ApplicantDetails, ApplicationDetails
from authentication.models import EndUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# create applicant details
class CreateApplicantDetailsView(generics.CreateAPIView):
    serializer_class = ApplicantDetailsSerializer
    permission_classes = [permissions.IsAuthenticated & IsUser]
    queryset = ApplicantDetails.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
# create application details
class CreateApplicationDetailsView(generics.CreateAPIView):
    serializer_class = ApplicationDetailsSerializer
    permission_classes = [permissions.IsAuthenticated & IsUser]
    queryset = ApplicationDetails.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# get applicant details
class GetApplicantDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsUser]
    @swagger_auto_schema(
        operation_description="Get applicant details",
        responses={status.HTTP_200_OK: openapi.Response("Applicant details", schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "full_name": openapi.Schema(type=openapi.TYPE_STRING, description="Full name of the applicant"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email address of the applicant"),
                "resume_link": openapi.Schema(type=openapi.TYPE_STRING, description="Link to the applicant's resume"),
                "portfolio_link": openapi.Schema(type=openapi.TYPE_STRING, description="Link to the applicant's portfolio"),
            }
        ))}
    )
    def get(self, request):
        user_obj= EndUser.objects.get(user=request.user)
        applicant = ApplicantDetails.objects.get(user=request.user)
        output = {
            "full_name": user_obj.first_name + " " + user_obj.last_name,
            "email": request.user.email,
            "resume_link": applicant.resume_link,
            "portfolio_link": applicant.portfolio_link
        }
        return response.Response(output, status=status.HTTP_200_OK)
       
# get user applications details
class ListUserApplicationsView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsUser]
    
    @swagger_auto_schema(
        operation_description="List user applications",
        responses={status.HTTP_200_OK: openapi.Response("List of user applications", schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "pk": openapi.Schema(type=openapi.TYPE_INTEGER, description="Application ID"),
                    "position": openapi.Schema(type=openapi.TYPE_STRING, description="Position applied for"),
                    "status": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(
                        type=openapi.TYPE_STRING,
                        enum=["Applying", "Offered", "Rejected", "Submitted"])),
                    "application_date": openapi.Schema(type=openapi.TYPE_STRING, description="Date of application"),
                    "job_link": openapi.Schema(type=openapi.TYPE_STRING, description="url to the job posting"),
                    "location": openapi.Schema(type=openapi.TYPE_STRING, description="Location of the job posting"),
                }
            )
        ))}
    )
    def get(self, request):
        applications = ApplicationDetails.objects.filter(user=request.user)
        serializer = ApplicationDetailsSerializer(applications, many=True)
        return response.Response(serializer.data)
    
# update applicant details
class UpdateApplicantDetailsView(generics.GenericAPIView):
    serializer_class = ApplicantDetailsSerializer
    permission_classes = [permissions.IsAuthenticated & IsUser]
    
    def patch(self, request):
        applicant = ApplicantDetails.objects.get(user=request.user)
        serializer = self.serializer_class(applicant, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
# update application details
class UpdateApplicationView(generics.GenericAPIView):
    serializer_class = ApplicationDetailsSerializer
    permission_classes = [permissions.IsAuthenticated & IsUser]
    
    @swagger_auto_schema(
        operation_description="Update application details",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Application ID",
                required=True
            )
        ])
    def patch(self, request):
        id = self.request.query_params.get('id')
        application = ApplicationDetails.objects.get(user=request.user, pk=id)
        serializer = self.serializer_class(application, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
# delete application details
class DeleteApplicationView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsUser]
    
    @swagger_auto_schema(
        operation_description="Delete an application",
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Application ID",
                required=True
            )
        ],
        responses={status.HTTP_204_NO_CONTENT: "Application deleted successfully"}
    )
    def delete(self, request):
        id = self.request.query_params.get('id')
        application = ApplicationDetails.objects.get(user=request.user, pk=id)
        application.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)