from django import forms
from paymentapp.models import BillingAddress


class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'zipode', 'city', 'country', ]
