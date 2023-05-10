import os

from twilio.rest import Client
from celery import Celery, shared_task

import time

app = Celery('tasks', broker='pyamqp://guest@localhost//')

account_sid = "AC26d024765dd65bdc1ef4528418061433"
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
auth_token = "5184fbc258757930ac7d7532e584cd26"
verify_sid = "VA75ebef320b64c2b8147df8fa4bbf4ee0"
# verified_number = "+380955518311"
client = Client(account_sid, auth_token)



@shared_task
def send_sms(number):
    print("Start send SMS task")

    verification = client.verify.v2.services(verify_sid).verifications.create(to=number, channel="sms")
    print(verification.status)

    time.sleep(10)
    print("End send SMS task")
    return True


@shared_task
def check_otp(verified_number, otp_code):
    print("Start check code")

    verification_check = client.verify.v2.services(verify_sid).verification_checks.create(to=verified_number, code=otp_code)
    print(verification_check.status)

    print("End check code")
    return verification_check.status
