from django import forms
from .models import Requisition

class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = [
            'doc_number',
            'department',
            'requisition_by',
            'remarks'
        ]
        widgets = {
            'doc_number': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-generated (e.g., REQ-0001)'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'requisition_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter requester name'
            }),
            'remarks': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter remarks'
            }),
        }
        labels = {
            'doc_number': 'Document Number',
            'department': 'Department',
            'requisition_by': 'Requisition By',
            'remarks': 'Remarks'
        }
        help_texts = {
            'doc_number': 'Unique document number for the requisition',
            'department': 'Department requesting the items',
            'requisition_by': 'Name of the person making the requisition',
            'remarks': 'Additional remarks or notes'
        }
