from django import forms
from .models import Guest


class GuestRegisterForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = (
            'fullname',
            'mobile',
            'insurance_company',
            'dispensing_pharmacy',
            # 'dispensing_pharmacist',
            'dipensing_date',
            'next_dispensing',
        )

    def __init__(self, *args, **kwargs):
        super(GuestRegisterForm, self).__init__(*args, **kwargs)
        self.fields['dispensing_pharmacy'].empty_label = 'Select'
        # self.fields['dispensing_pharmacist'].empty_label = 'Select'
        # self.fields['dispensing_pharmacist'].required = False
