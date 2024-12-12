# forms.py
from django import forms
from .models import PricingInquiry

class PricingInquiryForm(forms.ModelForm):
    class Meta:
        model = PricingInquiry
        fields = [
            'company_name', 
            'contact_person', 
            'phone', 
            'email', 
            'number_of_employees', 
            'enquiry_message', 
            'plan_name', 
            'plan_amount'
        ]
        
    # Optionally, add some custom validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone
