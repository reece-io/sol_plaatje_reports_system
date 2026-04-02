from django import forms
from .models import Fault
from django.core.exceptions import ValidationError 

class FaultForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = ['nature', 'location', 'reporter_name', 'contact_number']

    def clean_contact_number(self):
        contact = self.cleaned_data.get('contact_number')
        
        if not contact.isdigit():
            raise ValidationError("Contact number must only contain digits.")
        
        if len(contact) != 10:
            raise ValidationError("Contact number must be exactly 10 digits long beginning with 0.")
            
        return contact