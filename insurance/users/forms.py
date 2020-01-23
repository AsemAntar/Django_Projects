from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import Pharmacist


class MyValidator(UnicodeUsernameValidator):
    regex = r'[0-9]'


class CustomRegisterForm(forms.Form):
    username = forms.CharField(label='Pharmacy Code', max_length=4, min_length=4,
                               help_text='Required. 4 characters. Digits only.', error_messages={'required': 'Not Valid'})

    email = forms.EmailField(label='Email', help_text='Enter a valid email')

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                                help_text=(
                                    '1. Password should consist of numbers and digits. <br/>2. Special Characters are allowed. <br/>3. The best example of a password is your favorite movie quote. <br/>4. Example: 1l0ve_avengers+Endgame'
                                ))

    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput, help_text='Enter the same password again')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        user = User.objects.filter(username=username)
        if user.count():
            raise ValidationError('Username already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user = User.objects.filter(email=email)
        if user.count():
            raise ValidationError('Email already exist')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password doesn't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

    def __init__(self, *args, **kwargs):
        super(CustomRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(MyValidator())


class PharmacistForm(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = ('name', 'emp_code')
        labels = {
            'name': 'Pharmacist Name',
            'emp_code': 'Employee Code'
        }

    def __init__(self, *args, **kwargs):
        super(PharmacistForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'mb-5'
        # self.fields['emp_code'].widget.attrs['class'] = 'mb-5'

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(UserRegisterForm, self).__init__(*args, **kwargs)
#         self.fields['username'].required = False
