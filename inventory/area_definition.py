from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Existing forms...
class Area(forms.Form):
    """Form for managing geographic/operational areas in the ERP system."""
    
    area_code = forms.CharField(
        label="Area Code",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'placeholder': 'Auto-generated (e.g., AREA-0001)'
        }),
        required=False,
        help_text="System generated unique identifier"
    )
    
    area_name = forms.CharField(
        label="Area Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter area name'
        }),
        help_text="Descriptive name for the operational area"
    )
    
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    status = forms.ChoiceField(
        label="Status",
        choices=STATUS_CHOICES,
        initial='active',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    area_description = forms.CharField(
        label="Area Description",
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Optional description of the area'
        }),
        help_text="Additional details about the area's purpose or characteristics"
    )
        
    
    def clean_area_code(self):
        """Validate that area code is positive."""
        area_code = self.cleaned_data.get('area_code')
        if area_code and area_code <= 0:
            raise ValidationError("Area code must be a positive number.")
        return area_code

