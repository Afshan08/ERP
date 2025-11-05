from django import forms
from .models import IssueTransaction

class IssueTransactionForm(forms.ModelForm):
    class Meta:
        model = IssueTransaction
        fields = [
            'transaction_no',
            'date',
            'nature',
            'area',
            'department',
            'customer',
            'lot_no',
            'dc_no',
            'material'
        ]
        widgets = {
            'transaction_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter transaction number'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'nature': forms.Select(attrs={
                'class': 'form-control'
            }),
            'area': forms.Select(attrs={
                'class': 'form-control'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'customer': forms.Select(attrs={
                'class': 'form-control'
            }),
            'lot_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lot number'
            }),
            'dc_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter D/C number'
            }),
            'material': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter material'
            }),
        }
        labels = {
            'transaction_no': 'Transaction Number',
            'date': 'Date',
            'nature': 'Nature',
            'area': 'Area',
            'department': 'Department',
            'customer': 'Customer',
            'lot_no': 'Lot Number',
            'dc_no': 'D/C Number',
            'material': 'Material'
        }
        help_texts = {
            'transaction_no': 'Unique transaction number',
            'date': 'Date of the transaction',
            'nature': 'Nature of the transaction',
            'area': 'Area for the transaction',
            'department': 'Department involved',
            'customer': 'Customer for the transaction',
            'lot_no': 'Lot number',
            'dc_no': 'D/C number',
            'material': 'Material details'
        }
