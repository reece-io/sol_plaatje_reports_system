from django import forms
from .models import Fault
from django.utils.html import strip_tags

class FaultForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = ['nature', 'location', 'reporter_name', 'contact_number']

    def clean_reporter_name(self):
        name = self.cleaned_data.get('reporter_name')
        # strip_tags removes any <script> or <html> tags for XSS protection
        return strip_tags(name)

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if len(location) < 10:
            raise forms.ValidationError("Please provide a more detailed address.")
        return strip_tags(location)