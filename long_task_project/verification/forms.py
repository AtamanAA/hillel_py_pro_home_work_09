from django import forms
from django.core.exceptions import ValidationError
import phonenumbers


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=20, initial="+380 XX XXX XX XX")

    def clean_phone(self):
        phone_raw = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone_raw, None)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Phone isn't valid!")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone isn't valid!")
        return phonenumbers.format_number(
            phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )


class CodeForm(forms.Form):
    code = forms.CharField(max_length=6, initial="XXXXXX")
