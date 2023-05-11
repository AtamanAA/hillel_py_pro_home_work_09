from celery import Celery, shared_task
from dotenv import dotenv_values
from twilio.rest import Client


app = Celery("tasks", broker="pyamqp://guest@localhost//")

env_var = dotenv_values(".env")
TWILIO_AUTH_TOKEN = env_var["TWILIO_AUTH_TOKEN"]
account_sid = "AC26d024765dd65bdc1ef4528418061433"
verify_sid = "VA75ebef320b64c2b8147df8fa4bbf4ee0"
client = Client(account_sid, TWILIO_AUTH_TOKEN)


@shared_task
def send_code_by_sms(number):
    verification = client.verify.v2.services(verify_sid).verifications.create(
        to=number, channel="sms"
    )
    return verification.status


@shared_task
def check_otp(verified_number, otp_code):
    verification_check = client.verify.v2.services(
        verify_sid
    ).verification_checks.create(to=verified_number, code=otp_code)
    return verification_check.status
