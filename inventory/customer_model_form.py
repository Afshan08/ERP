from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Customer

class CustomerModelForm(forms.ModelForm):
    """Model form for managing customer information in the ERP system."""
    
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        
        widgets = {
            'customer_code': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-generated (e.g., CUST-0001)'
            }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full customer/company name'
            }),
            'contact_person_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name of primary contact'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'contact@customer.com'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 123-4567'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
            'payment_terms': forms.Select(attrs={'class': 'form-control'}),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.customer.com'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any additional information about the customer'
            }),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'is_preferred': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        help_texts = {
            'customer_id': 'Leave blank for new customers',
            'customer_name': 'Official registered business or individual name',
            'contact_person_name': 'Main point of contact for the customer',
            'contact_email': 'Primary email address',
            'contact_phone': 'Primary contact phone number',
            'country': 'Country',
            'customer_type': 'Type of customer',
            'payment_terms': 'Payment terms',
            'website': 'Website URL',
            'notes': 'Any additional information about the customer',
            'status': 'Customer status',
            'is_preferred': 'Preferred customer',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial values
        self.fields['country'].initial = 'Pakistan'
        self.fields['currency'].initial = 'PKR'
    
    def clean_customer_name(self):
        """Validate customer name is not empty."""
        customer_name = self.cleaned_data.get('customer_name')
        if not customer_name or not customer_name.strip():
            raise ValidationError("Customer name is required.")
        return customer_name.strip()
    
    def clean_contact_email(self):
        """Validate email format."""
        email = self.cleaned_data.get('contact_email')
        if email:
            email = email.lower()
            if not email.endswith(('.com', '.org', '.net', '.edu', '.gov')):
                raise ValidationError("Please enter a valid email address.")
        return email
    
    def clean(self):
        """Cross-field validation."""
        cleaned_data = super().clean()
        
        # Ensure at least one contact method is provided
        email = cleaned_data.get('contact_email')
        phone = cleaned_data.get('contact_phone')
        
        if not email and not phone:
            raise ValidationError(
                "At least one contact method (email or phone) is required."
            )
        
        return cleaned_data
