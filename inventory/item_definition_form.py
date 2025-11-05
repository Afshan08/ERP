from django import forms
from .models import ItemDefinition

class ItemDefinitionForm(forms.ModelForm):
    class Meta:
        model = ItemDefinition
        fields = [
            'item_code',
            'item_name',
            'specification',
            'base_item',
            'item_category',
            'salestax_type',
            'unit_of_measure',
            'std_cost',
            'important',
            'active'
        ]
        widgets = {
            'item_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item code'
            }),
            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter item name'
            }),
            'specification': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter item specification'
            }),
            'base_item': forms.Select(attrs={
                'class': 'form-control'
            }),
            'item_category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'salestax_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'unit_of_measure': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., kg, pcs, liters'
            }),
            'std_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'important': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'item_code': 'Item Code',
            'item_name': 'Item Name',
            'specification': 'Specification',
            'base_item': 'Base Item (for variants)',
            'item_category': 'Item Category',
            'salestax_type': 'Sales Tax Type',
            'unit_of_measure': 'Unit of Measure',
            'std_cost': 'Standard Cost',
            'important': 'Mark as Important',
            'active': 'Active'
        }
        help_texts = {
            'item_code': 'Unique code for the item',
            'item_name': 'Descriptive name of the item',
            'specification': 'Detailed specifications',
            'base_item': 'Select if this is a variant of another item',
            'item_category': 'Category this item belongs to',
            'salestax_type': 'Type of sales tax applicable',
            'unit_of_measure': 'Unit used for measurement (e.g., kg, pcs)',
            'std_cost': 'Standard cost per unit',
            'important': 'Check if this is an important item',
            'active': 'Uncheck to deactivate the item'
        }
