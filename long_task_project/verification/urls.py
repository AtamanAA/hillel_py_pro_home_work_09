from django.urls import path

from . import views


urlpatterns = [
    path("", views.verification, name="verification"),
    # path("check-code", views.check_code, name="check_code"),
    # path("done/", views.done, name="done"),
]