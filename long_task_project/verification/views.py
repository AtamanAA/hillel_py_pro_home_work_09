from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PhoneForm, CodeForm
from .tasks import send_sms, check_otp


def verification(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            send_sms.delay(phone)
            return HttpResponseRedirect(
                reverse("check_code", args=[phone])
            )

    else:
        form = PhoneForm()
    return render(request, "verification/index.html", {"form": form})


def check_code(request, phone):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            if check_otp(phone, code) == "approved":
                return redirect("sms_done")
            else:
                form = CodeForm()
                return render(request, "verification/check_code.html", {"form": form})  # Refactor!!!
    else:
        form = CodeForm()  # Should be error!!
    return render(request, "verification/check_code.html", {"form": form, "phone": phone})


def sms_done(request):
    return render(request, "verification/send_sms_done.html")
