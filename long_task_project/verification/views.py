from django.contrib import messages

from django.shortcuts import render, redirect

from .forms import PhoneForm
from .tasks import send_sms


def verification(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            print(phone)
            send_sms.delay()
        return redirect("sms_done")
    else:
        form = PhoneForm()
    return render(request, "verification/index.html", {"form": form})


def sms_done(request):
    return render(request, "verification/send_sms_done.html")
