from django import forms
from django.core.exceptions import ValidationError
from .models import Purchase

class PurchaseModelForm(forms.ModelForm):
    """Model form for managing purchase orders in the ERP system."""

    class Meta:
        model = Purchase
        fields = ['supplier', 'purchase_date', 'total_amount', 'currency', 'status', 'notes']
        exclude = ['created_at', 'updated_at']

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control',
            }),
            'purchase_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'total_amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'currency': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Any additional notes about the purchase'
            }),
        }

        help_texts = {
            'supplier': 'Select the supplier for this purchase',
            'purchase_date': 'Date when the purchase order was made',
            'total_amount': 'Total amount of the purchase',
            'currency': 'Currency for the purchase amount',
            'status': 'Current status of the purchase order',
            'notes': 'Additional notes about the purchase',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial values
        from django.utils import timezone
        if not self.instance.pk:
            self.fields['purchase_date'].initial = timezone.now().date()
            self.fields['currency'].initial = 'PKR'

    def clean_total_amount(self):
        """Validate total amount is positive."""
        total_amount = self.cleaned_data.get('total_amount')
        if total_amount is not None and total_amount <= 0:
            raise ValidationError("Total amount must be greater than zero.")
        return total_amount

    def clean_purchase_date(self):
        """Validate purchase date is not in the future."""
        purchase_date = self.cleaned_data.get('purchase_date')
        from django.utils import timezone
        if purchase_date and purchase_date > timezone.now().date():
            raise ValidationError("Purchase date cannot be in the future.")
        return purchase_date

    def clean(self):
        """Cross-field validation."""
        cleaned_data = super().clean()

        # Ensure supplier is active
        supplier = cleaned_data.get('supplier')
        if supplier and supplier.status != 'active':
            raise ValidationError("Cannot create purchase for inactive supplier.")

        return cleaned_data
