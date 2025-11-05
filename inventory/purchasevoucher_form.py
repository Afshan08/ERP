from django import forms
from .models import PurchaseVoucher

class PurchaseVoucherForm(forms.ModelForm):
    class Meta:
        model = PurchaseVoucher
        fields = [
            'transaction_no',
            'transaction_type',
            'transaction_date',
            'supplier',
            'bill_no',
            'st_inv_no',
            'bilty_no',
            'days'
        ]
        widgets = {
            'transaction_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter transaction number'
            }),
            'transaction_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'transaction_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control'
            }),
            'bill_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter bill number'
            }),
            'st_inv_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter S/T invoice number'
            }),
            'bilty_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter bilty number'
            }),
            'days': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter number of days'
            }),
        }
        labels = {
            'transaction_no': 'Transaction Number',
            'transaction_type': 'Transaction Type',
            'transaction_date': 'Transaction Date',
            'supplier': 'Supplier',
            'bill_no': 'Bill Number',
            'st_inv_no': 'S/T Invoice Number',
            'bilty_no': 'Bilty Number',
            'days': 'Days'
        }
        help_texts = {
            'transaction_no': 'Unique transaction number',
            'transaction_type': 'Type of transaction',
            'transaction_date': 'Date of the transaction',
            'supplier': 'Supplier for the voucher',
            'bill_no': 'Bill number',
            'st_inv_no': 'S/T invoice number',
            'bilty_no': 'Bilty number',
            'days': 'Number of credit or delivery days'
        }
