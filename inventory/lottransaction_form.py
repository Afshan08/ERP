from django import forms
from .models import LotTransaction

class LotTransactionForm(forms.ModelForm):
    class Meta:
        model = LotTransaction
        fields = [
            'doc_no',
            'date',
            'customer',
            'gray_receipt_no',
            'dc_no',
            'lot_no',
            'nature',
            'start_date',
            'end_date',
            'remarks'
        ]
        widgets = {
            'doc_no': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-generated (e.g., LOT-0001)'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control'
            }),
            'gray_receipt_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter gray receipt number'
            }),
            'dc_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter D/C number'
            }),
            'lot_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lot number'
            }),
            'nature': forms.Select(attrs={
                'class': 'form-control'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter remarks'
            }),
        }
        labels = {
            'doc_no': 'Document Number',
            'date': 'Date',
            'customer': 'Customer',
            'gray_receipt_no': 'Gray Receipt Number',
            'dc_no': 'D/C Number',
            'lot_no': 'Lot Number',
            'nature': 'Nature',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'remarks': 'Remarks'
        }
        help_texts = {
            'doc_no': 'Unique document number',
            'date': 'Date of the transaction',
            'customer': 'Customer for the lot',
            'gray_receipt_no': 'Gray receipt number',
            'dc_no': 'D/C number',
            'lot_no': 'Lot number',
            'nature': 'Nature of the transaction',
            'start_date': 'Start date',
            'end_date': 'End date',
            'remarks': 'Additional remarks'
        }
