from django.urls import path

from . import views


urlpatterns = [
    path("", views.verification, name="verification"),
    path("check-code/<phone>", views.check_code, name="check_code"),
    path("send-sms-done/", views.sms_done, name="sms_done"),
]
