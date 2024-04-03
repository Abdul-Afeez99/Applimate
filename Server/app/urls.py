from django.urls import path
from .views import (
    GetApplicantDetailsView, ListUserApplicationsView, CreateApplicantDetailsView,
    CreateApplicationDetailsView, UpdateApplicantDetailsView, UpdateApplicationView,
    DeleteApplicationView
)

urlpatterns = [
    path('applicants/register', CreateApplicantDetailsView.as_view(), name='create_applicant_details'),
    path('applications/register', CreateApplicationDetailsView.as_view(), name='create_application'),
    path('applicant-details/', GetApplicantDetailsView.as_view(), name='get_applicant_details'),
    path('applications/all', ListUserApplicationsView.as_view(), name='get_applications'),
    path('applicants/update', UpdateApplicantDetailsView.as_view(), name='update_applicant_details'),
    path('applications/update', UpdateApplicationView.as_view(), name='update_application'),
    path('applications/delete', DeleteApplicationView.as_view(), name='delete_application')
]
