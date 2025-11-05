from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class SupplierForm(forms.Form):
    """Comprehensive form for managing supplier information in the ERP system."""
    
    # Basic Information
    supplier_id = forms.IntegerField(
        label="Supplier ID",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Give an id to the supplier'
        }),
        required=False,
        help_text="Leave blank for new suppliers"
    )
    
    supplier_name = forms.CharField(
        label="Supplier Name",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter full supplier/company name'
        }),
        help_text="Official registered business name"
    )
    
    # Contact Information
    contact_person_name = forms.CharField(
        label="Primary Contact Person",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full name of primary contact'
        }),
        help_text="Main point of contact at the supplier"
    )
    
    contact_email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'contact@supplier.com'
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

    # Business Information
    BUSINESS_TYPE_CHOICES = [
        ('manufacturer', 'Manufacturer'),
        ('distributor', 'Distributor'),
        ('wholesaler', 'Wholesaler'),
        ('retailer', 'Retailer'),
        ('service_provider', 'Service Provider'),
        ('contractor', 'Contractor'),
        ('consultant', 'Consultant'),
        ('other', 'Other'),
    ]
    
    business_type = forms.ChoiceField(
        label="Business Type",
        choices=BUSINESS_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    ntn_number = forms.CharField(
        label="NTN Number",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Company National Tax Number'
        }),
        help_text="National Tax Number"
    )
    
    city = forms.CharField(
        label="City",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'City'
        })
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
    
    # Financial Information
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
    
    currency = forms.ChoiceField(
        label="Preferred Currency",
        choices=[
            ('USD', 'US Dollar'),
            ('EUR', 'Euro'),
            ('GBP', 'British Pound'),
            ('CAD', 'Canadian Dollar'),
            ('AUD', 'Australian Dollar'),
            ('JPY', 'Japanese Yen'),
            ('PKR', "Pakistani Rupees")
        ],
        initial='PKR',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Additional Information
    website = forms.URLField(
        label="Website",
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'https://www.supplier.com'
        })
    )
    
    notes = forms.CharField(
        label="Additional Notes",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Any additional information about the supplier'
        })
    )
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('pending_approval', 'Pending Approval'),
    ]
    
    status = forms.ChoiceField(
        label="Supplier Status",
        choices=STATUS_CHOICES,
        initial='active',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    is_preferred = forms.BooleanField(
        label="Preferred Supplier",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    def clean_supplier_name(self):
        """Validate supplier name is not empty."""
        supplier_name = self.cleaned_data.get('supplier_name')
        if not supplier_name or not supplier_name.strip():
            raise ValidationError("Supplier name is required.")
        return supplier_name.strip()
    
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


