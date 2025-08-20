from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class AreaForm(models.Model):
    """Model for managing geographic/operational areas in the ERP system."""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    areacode = models.IntegerField(
        unique=True,
        null=False,
        blank=False,
        help_text="Unique numeric identifier for the area (1-9999)"
    )
    
    areaname = models.CharField(
        max_length=100,
        help_text="Descriptive name for the operational area"
    )
    
    area_description = models.TextField(
        blank=True,
        null=True,
        help_text="Additional details about the area's purpose or characteristics"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Current operational status of the area"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'areas'
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['areacode']
    
    def __str__(self):
        return f"{self.areacode} - {self.areaname}"



class Supplier(models.Model):
    """Comprehensive model for managing supplier information in the ERP system."""
    
    BUSINESS_TYPE_CHOICES = [
        ('manufacturer', 'Manufacturer'),
        ('distributor', 'Distributor'),
        ('wholesaler', 'Wholesaler'),
        ('retailer', 'Retailer'),
        ('service_provider', 'Service Provider'),
        ('contractor', 'Contractor'),
        ('consultant', 'Consultant'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('pending_approval', 'Pending Approval'),
    ]
    
    PAYMENT_TERMS_CHOICES = [
        ('net_15', 'Net 15'),
        ('net_30', 'Net 30'),
        ('net_45', 'Net 45'),
        ('net_60', 'Net 60'),
        ('cod', 'Cash on Delivery'),
        ('prepaid', 'Prepaid'),
    ]
    
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar'),
        ('JPY', 'Japanese Yen'),
        ('PKR', "Pakistani Rupees"),
    ]
    
    # Basic Information
    supplier_id = models.IntegerField(
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated if new"
    )
    
    supplier_name = models.CharField(
        max_length=200,
        help_text="Official registered business name"
    )
    
    # Contact Information
    contact_person_name = models.CharField(
        max_length=100,
        help_text="Main point of contact at the supplier"
    )
    
    contact_email = models.EmailField(
        help_text="Primary email address"
    )
    
    contact_phone = models.CharField(
        max_length=12,
        validators=[RegexValidator(
            regex=r'^\+?[\d\s\-\(\)]+$',
            message='Enter a valid phone number'
        )],
        help_text="Primary contact phone number"
    )
    
    # Business Information
    business_type = models.CharField(
        max_length=20,
        choices=BUSINESS_TYPE_CHOICES,
        help_text="Type of business"
    )
    
    ntn_number = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="National Tax Number"
    )
    
    country = models.CharField(
        max_length=100,
        default='United States',
        help_text="Country"
    )
    
    # Financial Information
    payment_terms = models.CharField(
        max_length=20,
        choices=PAYMENT_TERMS_CHOICES,
        default='net_30',
        help_text="Payment terms"
    )
    
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='USD',
        help_text="Preferred currency"
    )
    
    # Additional Information
    website = models.URLField(
        blank=True,
        null=True,
        help_text="Website URL"
    )
    
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional information about the supplier"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Supplier status"
    )
    
    is_preferred = models.BooleanField(
        default=False,
        help_text="Preferred supplier"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['supplier_name']
    
    def __str__(self):
        return f"{self.supplier_name} ({self.supplier_id or 'New'})"
    
    def get_primary_contact(self):
        """Return primary contact information."""
        return {
            'name': self.contact_person_name,
            'email': self.contact_email,
            'phone': self.contact_phone,
        }


# Customer form 
class Customer(models.Model):
    """Comprehensive model for managing customer information in the ERP system."""
    
    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('business', 'Business'),
        ('government', 'Government'),
        ('non_profit', 'Non-Profit'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('pending_approval', 'Pending Approval'),
    ]
    
    PAYMENT_TERMS_CHOICES = [
        ('net_15', 'Net 15'),
        ('net_30', 'Net 30'),
        ('net_45', 'Net 45'),
        ('net_60', 'Net 60'),
        ('cod', 'Cash on Delivery'),
        ('prepaid', 'Prepaid'),
    ]
    
    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('CAD', 'Canadian Dollar'),
        ('AUD', 'Australian Dollar'),
        ('JPY', 'Japanese Yen'),
        ('PKR', "Pakistani Rupees"),
    ]
    
    # Basic Information
    customer_id = models.IntegerField(
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated if new"
    )
    
    customer_name = models.CharField(
        max_length=200,
        help_text="Official registered business or individual name"
    )
    
    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPE_CHOICES,
        help_text="Type of customer"
    )
    
    # Contact Information
    contact_person_name = models.CharField(
        max_length=100,
        help_text="Main point of contact for the customer"
    )
    
    contact_email = models.EmailField(
        help_text="Primary email address"
    )
    
    contact_phone = models.CharField(
        max_length=12,
        validators=[RegexValidator(
            regex=r'^\+?[\d\s\-\(\)]+$',
            message='Enter a valid phone number'
        )],
        help_text="Primary contact phone number"
    )
    
    
    
    country = models.CharField(
        max_length=100,
        default='Pakistan',
        help_text="Country"
    )

    
    payment_terms = models.CharField(
        max_length=20,
        choices=PAYMENT_TERMS_CHOICES,
        default='net_30',
        help_text="Payment terms"
    )
    
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='PKR',
        help_text="Preferred currency"
    )
    
    # Additional Information
    website = models.URLField(
        blank=True,
        null=True,
        help_text="Website URL"
    )
    
    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Any additional information about the customer"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        help_text="Customer status"
    )
    
    is_preferred = models.BooleanField(
        default=False,
        help_text="Preferred customer"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['customer_name']
    
    def __str__(self):
        return f"{self.customer_name} ({self.customer_id or 'New'})"
    
    
    def get_primary_contact(self):
        """Return primary contact information."""
        return {
            'name': self.contact_person_name,
            'email': self.contact_email,
            'phone': self.contact_phone,
        }


