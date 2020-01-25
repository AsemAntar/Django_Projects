from django import forms
from .models import Guest, Medication
# from users.models import Pharmacist
# from django_currentuser.middleware import get_current_authenticated_user


class GuestRegisterForm(forms.ModelForm):
    # dispensing_pharmacist = forms.ChoiceField(widget=forms.Select)

    class Meta:
        model = Guest
        fields = (
            'fullname',
            'mobile',
            'insurance_company',
            # 'dispensing_pharmacy',
            # 'dispensing_pharmacist',
            'dipensing_date',
            'next_dispensing',
        )

    def __init__(self, *args, **kwargs):
        # get the current logged in user
        # user = get_current_authenticated_user()
        super(GuestRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['dispensing_pharmacy'].empty_label = 'Select'

        # limit pharmacist choices to only logged in user
        # PHARMACIST_CHOICES = Pharmacist.objects.filter(working_at=user)
        # self.fields['dispensing_pharmacist'].choices = tuple(
        #     enumerate(PHARMACIST_CHOICES))


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ('name', 'dose', 'frequency', 'quantity')
