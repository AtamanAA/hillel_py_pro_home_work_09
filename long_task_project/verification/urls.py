from django.urls import path

from . import views


urlpatterns = [
    path("", views.verification, name="verification"),
    path("send-sms-done/", views.sms_done, name="sms_done"),
    # path("check-code", views.check_code, name="check_code"),
    # path("done/", views.done, name="done"),
]