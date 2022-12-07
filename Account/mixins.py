from django.conf import settings
from twilio.rest import Client


class MessageHandler:
    phone_number = None
    otp = None
    
    def __init__(self,phone_number,otp):
        self.otp = otp
        self.phone_number = phone_number
        
    def send_otp_to_phone(self):
        client = Client(settings.TWILIO_SID, settings.TWILIO_AUTH)

        message = client.messages.create(
                                    body=f'OTP: {self.otp}',
                                    from_='+13609972330',
                                    to= self.phone_number
                                )

        print(message.sid)