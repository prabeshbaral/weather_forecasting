
from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(max_length=255, label='Enter Address', widget=forms.TextInput(attrs={'placeholder': 'Enter address here'}))
