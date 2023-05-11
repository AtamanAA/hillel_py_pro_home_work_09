from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from twilio.base.exceptions import TwilioRestException

from .forms import PhoneForm, CodeForm
from .tasks import send_code_by_sms, check_otp


def verification(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            send_code_by_sms.delay(phone)
            return HttpResponseRedirect(reverse("check_code", args=[phone]))
    else:
        form = PhoneForm()
    return render(request, "verification/index.html", {"form": form})


def check_code(request, phone):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            try:
                if check_otp(phone, code) == "approved":
                    return redirect("verification_done")
                else:
                    messages.error(request, f"Code doesn't math. Try again!")
            except TwilioRestException:
                messages.error(request, f"Code is invalid. Try again!")
            return HttpResponseRedirect(reverse("check_code", args=[phone]))
    else:
        form = CodeForm()
    return render(
        request, "verification/check_code.html", {"form": form, "phone": phone}
    )


def verification_done(request):
    return render(request, "verification/verification_done.html")
