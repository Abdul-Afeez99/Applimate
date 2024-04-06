from django.db import models
from authentication.models import CustomUser

# Applicant details
class ApplicantDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="applicant")
    resume_link = models.URLField(max_length=250)
    portfolio_link = models.URLField(max_length=250)
    
    
# Application details
class ApplicationDetails(models.Model):
    status_choice = [
        ("Applying", "Applying"),
        ("Offered", 'Offered'),
        ("Rejected", 'Rejected'),
        ("submitted", 'Submitted')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="applications")
    position = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status_choice, default="Applying")
    application_date = models.DateField(auto_now_add=True)
    job_link = models.URLField(max_length=250)
    location = models.CharField(max_length=200)
    