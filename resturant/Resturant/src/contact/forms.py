from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = PhoneNumberField(required=False)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
