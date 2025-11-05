from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class CustomerForm(forms.Form):
    """Comprehensive form for managing customer information in the ERP system."""
    
    # Basic Information
    customer_id = forms.IntegerField(
        label="Customer ID",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Give an id to the customer'
        }),
        required=False,
        help_text="Leave blank for new customers"
    )
    
    customer_name = forms.CharField(
        label="Customer Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter full customer/company name'
        }),
        help_text="Official registered business or individual name"
    )
    
    # Contact Information
    contact_person_name = forms.CharField(
        label="Primary Contact Person",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full name of primary contact'
        }),
        help_text="Main point of contact for the customer"
    )
    
    contact_email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'contact@customer.com'
        }),
        help_text="Primary email address"
    )
    
    contact_phone = forms.CharField(
        label="Phone Number",
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 123-4567'
        }),
        validators=[RegexValidator(
            regex=r'^\+?[\d\s\-\(\)]+$',
            message='Enter a valid phone number'
        )],
        help_text="Primary contact phone number"
    )

    country = forms.CharField(
        label="Country",
        max_length=100,
        initial='Pakistan',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Country'
        })
    )

    # Customer Type
    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
        ('government', 'Government'),
        ('non_profit', 'Non-Profit'),
    ]
    
    customer_type = forms.ChoiceField(
        label="Customer Type",
        choices=CUSTOMER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    
    payment_terms = forms.ChoiceField(
        label="Payment Terms",
        choices=[
            ('net_15', 'Net 15'),
            ('net_30', 'Net 30'),
            ('net_45', 'Net 45'),
            ('net_60', 'Net 60'),
            ('cod', 'Cash on Delivery'),
            ('prepaid', 'Prepaid'),
        ],
        initial='net_30',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Additional Information
    website = forms.URLField(
        label="Website",
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://www.customer.com'
        })
    )
    
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Any additional information about the customer'
        })
    )
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('pending_approval', 'Pending Approval'),
    ]
    
    status = forms.ChoiceField(
        label="Customer Status",
        choices=STATUS_CHOICES,
        initial='active',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    is_preferred = forms.BooleanField(
        label="Preferred Customer",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
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
