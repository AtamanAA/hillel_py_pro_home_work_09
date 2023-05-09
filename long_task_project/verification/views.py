from django.contrib import messages

from django.shortcuts import render, redirect

from .forms import PhoneForm


def verification(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            print(phone)
    else:
        form = PhoneForm()
    return render(request, "verification/index.html", {"form": form})
