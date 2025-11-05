from django import forms
from .models import ReceiptTransaction

class ReceiptTransactionForm(forms.ModelForm):
    class Meta:
        model = ReceiptTransaction
        fields = [
            'transaction_no',
            'transaction_date',
            'nature',
            'area',
            'delivery_challan_no',
            'supplier',
            'client_po',
            'remarks',
            'grir',
            'gpi_status',
            'gpo'
        ]
        widgets = {
            'transaction_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter transaction number'
            }),
            'transaction_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'nature': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter nature of transaction'
            }),
            'area': forms.Select(attrs={
                'class': 'form-control'
            }),
            'delivery_challan_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter delivery challan number'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control'
            }),
            'client_po': forms.Select(attrs={
                'class': 'form-control'
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter remarks'
            }),
            'grir': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter GRIR'
            }),
            'gpi_status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'gpo': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'transaction_no': 'Transaction Number',
            'transaction_date': 'Transaction Date',
            'nature': 'Nature',
            'area': 'Area',
            'delivery_challan_no': 'Delivery Challan Number',
            'supplier': 'Supplier',
            'client_po': 'Client PO',
            'remarks': 'Remarks',
            'grir': 'GRIR',
            'gpi_status': 'GPI Status',
            'gpo': 'GPO'
        }
        help_texts = {
            'transaction_no': 'Unique transaction number',
            'transaction_date': 'Date of the transaction',
            'nature': 'Nature of the transaction',
            'area': 'Area for the transaction',
            'delivery_challan_no': 'Delivery challan number',
            'supplier': 'Supplier involved',
            'client_po': 'Client purchase order',
            'remarks': 'Additional remarks',
            'grir': 'GRIR details',
            'gpi_status': 'GPI status',
            'gpo': 'GPO details'
        }
