from django import forms
from .models import PurchaseOrder

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = [
            'po_number',
            'po_date',
            'po_type',
            'station_code',
            'supplier',
            'remarks',
            'terms_conditions',
            'requisition',
            'ref_no',
            'delivery_at',
            'order_by',
            'condition',
            'freight',
            'quantity',
            'rate',
            'amount',
            'sales_tax',
            'discount',
            'requisition_number'
        ]
        widgets = {
            'po_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter PO number'
            }),
            'po_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'po_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter PO type'
            }),
            'station_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter station code'
            }),
            'supplier': forms.Select(attrs={
                'class': 'form-control'
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter remarks'
            }),
            'terms_conditions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter terms and conditions'
            }),
            'requisition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'ref_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter reference number'
            }),
            'delivery_at': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter delivery location'
            }),
            'order_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter order by'
            }),
            'condition': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter conditions'
            }),
            'freight': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'sales_tax': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'requisition_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter requisition number'
            }),
        }
        labels = {
            'po_number': 'PO Number',
            'po_date': 'PO Date',
            'po_type': 'PO Type',
            'station_code': 'Station Code',
            'supplier': 'Supplier',
            'remarks': 'Remarks',
            'terms_conditions': 'Terms and Conditions',
            'requisition': 'Requisition',
            'ref_no': 'Reference Number',
            'delivery_at': 'Delivery At',
            'order_by': 'Order By',
            'condition': 'Condition',
            'freight': 'Freight',
            'quantity': 'Quantity',
            'rate': 'Rate',
            'amount': 'Amount',
            'sales_tax': 'Sales Tax',
            'discount': 'Discount',
            'requisition_number': 'Requisition Number'
        }
        help_texts = {
            'po_number': 'Unique purchase order number',
            'po_date': 'Date of the purchase order',
            'po_type': 'Type of purchase order',
            'station_code': 'Station code',
            'supplier': 'Supplier for the purchase order',
            'remarks': 'Additional remarks',
            'terms_conditions': 'Terms and conditions of the order',
            'requisition': 'Related requisition',
            'ref_no': 'Reference number',
            'delivery_at': 'Delivery location',
            'order_by': 'Person who placed the order',
            'condition': 'Special conditions',
            'freight': 'Freight cost',
            'quantity': 'Quantity ordered',
            'rate': 'Rate per unit',
            'amount': 'Total amount',
            'sales_tax': 'Sales tax amount',
            'discount': 'Discount amount',
            'requisition_number': 'Requisition number'
        }
