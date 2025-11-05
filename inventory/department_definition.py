from django import forms 
from .models import DepartmentDefinition

class Department(forms.ModelForm):
    
    id = forms.IntegerField(
        label="Department ID",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',  # Use HTML correct spelling
            'placeholder': 'Department ID'
        })
    )
    class Meta:
        name = "departments"
        model = DepartmentDefinition
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Department name'
            }),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        # You don't really need to fetch `id` and `name` here unless validating
        return cleaned_data

    def save(self, commit=True):
        # Override save to ensure ID is set correctly for new instances
        instance = super().save(commit=False)

        if not instance.pk:
            last = DepartmentDefinition.objects.order_by('-id').first()
            instance.id = (last.id + 1) if last else 1

        if commit:
            instance.save()
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            # New form (not editing existing)
            last = DepartmentDefinition.objects.order_by('-id').first()
            next_id = last.id + 1 if last else 1
            self.fields['id'].initial = next_id  

