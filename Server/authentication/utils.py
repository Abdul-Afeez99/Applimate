from datetime import datetime
import pyotp
from django.core.mail import send_mail

class OTP():
    def __init__(self):
        self.totp = pyotp.TOTP(pyotp.random_base32(), interval=600)
        self.token = self.totp.now()
        
    #method to get generate OTP
    def getOTP(self):
        return self.token
        
    #method to send OTP
    def sendOTP(self, email):
        send_mail(
            subject='Email Verification',
            message=f'Your one-time verification is {self.token}',
            recipient_list= [email],
            fail_silently=False
        )
        