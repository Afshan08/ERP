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
    
    area_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated code (e.g., AREA-0001)"
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
    
    supplier_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated code (e.g., SUP-0001)"
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


class Purchase(models.Model):
    """Model for managing purchase orders in the ERP system."""

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending_approval', 'Pending Approval'),
        ('approved', 'Approved'),
        ('ordered', 'Ordered'),
        ('received', 'Received'),
        ('cancelled', 'Cancelled'),
    ]

    # Basic Information
    purchase_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='purchases',
        help_text="Supplier for this purchase"
    )

    purchase_date = models.DateField(
        help_text="Date of purchase order"
    )

    # Financial Information
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total purchase amount"
    )

    currency = models.CharField(
        max_length=3,
        choices=[
            ('USD', 'US Dollar'),
            ('EUR', 'Euro'),
            ('GBP', 'British Pound'),
            ('CAD', 'Canadian Dollar'),
            ('AUD', 'Australian Dollar'),
            ('JPY', 'Japanese Yen'),
            ('PKR', "Pakistani Rupees"),
        ],
        default='PKR',
        help_text="Currency for the purchase"
    )

    # Status and Notes
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        help_text="Current status of the purchase"
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Additional notes about the purchase"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'purchases'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
        ordering = ['-purchase_date']

    def __str__(self):
        return f"Purchase {self.purchase_id} - {self.supplier.supplier_name} - {self.total_amount} {self.currency}"




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
    
    customer_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        help_text="Auto-generated code (e.g., CUST-0001)"
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


class DepartmentDefinition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "departments"
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        
    def __str__(self):
        return f"{self.id}: {self.name}"
    
    
class INVcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "inv_category"
        verbose_name = 'Inventory Category'
        verbose_name_plural = 'Inventory Categories'
        
    def __str__(self):
        return f"{self.id}: {self.name}"
    
class ItemDefinition(models.Model):
    SALESTAX_CHOICES = [
    ('GST', 'GST'),
    ('VAT', 'VAT'),
    ('EXEMPT', 'Exempt'),
    ]
    item_code = models.CharField(unique=True, max_length=50)
    item_name = models.CharField(max_length=250)
    specification = models.CharField(null=True, blank=True)
    base_item = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="variants")
    item_category = models.ForeignKey('INVcategory', on_delete=models.CASCADE, related_name="items")
    salestax_type = models.CharField(max_length=50, choices=SALESTAX_CHOICES)
    unit_of_measure = models.CharField(max_length=20)
    std_cost = models.DecimalField(max_digits=12, decimal_places=2)
    important = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "item_definition"
        verbose_name = 'Item Definition'
        verbose_name_plural = 'Item Definition'
    
    
    def __str__(self):
        return self.item_name
    

class Requisition(models.Model):
    doc_number = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey("DepartmentDefinition", on_delete=models.CASCADE)
    requisition_by = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = "requisition"
        verbose_name = 'Requisition'
        verbose_name_plural = 'Requisition'
    
    
    def __str__(self):
        return f"{self.doc_number} - {self.requisition_by}"
 
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    po_date = models.DateField()
    po_type = models.CharField(max_length=50)
    area = models.ForeignKey("AreaForm", on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
    remarks = models.TextField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    requisition = models.ForeignKey("Requisition", on_delete=models.CASCADE)
    ref_no = models.CharField(max_length=50, blank=True, null=True)
    delivery_at = models.CharField(max_length=250)
    order_by = models.CharField(max_length=100)
    condition = models.TextField(blank=True, null=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    requisition_number = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        db_table = "purchase_order"
        verbose_name = 'Purchase Order'
        verbose_name_plural = 'Purchase Orders'
    
    
    def __str__(self):
        return f"Purchase Order by {self.order_by}"
    

class ReceiptTransaction(models.Model):
    gpi_status_options = [
        ('Pending', 'pending'),
        ('Approved', 'approved'),
        ('Rejected', 'rejected'),
    ]
    transaction_no = models.CharField(max_length=50, unique=True)
    transaction_date = models.DateField()

    # Could also be a CharField with choices
    nature = models.CharField(max_length=100)

    area = models.ForeignKey('AreaForm', on_delete=models.CASCADE)
    delivery_challan_no = models.CharField(max_length=100, blank=True, null=True)  # or FK if modeled
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    client_po = models.ForeignKey('PurchaseOrder', on_delete=models.SET_NULL, null=True, blank=True, related_name='receipt_client_po')
    po = models.ForeignKey('PurchaseOrder', on_delete=models.SET_NULL, null=True, blank=True, related_name='grn_po')
    item = models.ForeignKey('ItemDefinition', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    st = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    remarks = models.TextField(blank=True, null=True)
    grir = models.CharField(max_length=100)
    
    # Could also be CharField with choices like: Pending / Approved / Rejected
    gpi_status = models.CharField(max_length=50, default='Pending', choices=gpi_status_options)

    gpo = models.ForeignKey('PurchaseOrder', on_delete=models.SET_NULL, null=True, blank=True, related_name='receipt_gpo')

        
    class Meta:
        db_table = "grn"
        verbose_name = 'GRN'
        verbose_name_plural = 'GRNs'

    
    def __str__(self):
        return f"GRN {self.transaction_no}"
    

class PurchaseVoucher(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
        ('Return', 'Return'),
        # Add more types as per your business logic
    ]

    transaction_no = models.CharField(max_length=20, unique=True)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()

    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    bill_no = models.CharField(max_length=50)
    st_inv_no = models.CharField("S/T Inv. No", max_length=50)
    bilty_no = models.CharField(max_length=50)
    days = models.PositiveIntegerField(help_text="Number of credit days or delivery days")

            
    class Meta:
        db_table = "purchase_voucher"
        verbose_name = 'Purchase Voucher'
        verbose_name_plural = 'Purchase Vouchers'
    
    def __str__(self):
        return f"Voucher {self.transaction_no} - {self.transaction_type}"
    

class LotTransaction(models.Model):
    NATURE_CHOICES = [
        ('Dyeing', 'Dyeing'),
        ('Bleaching', 'Bleaching'),
        ('Finishing', 'Finishing'),
        # Add more as needed
    ]

    doc_no = models.CharField("Document No", max_length=20, unique=True)
    date = models.DateField()
    customer = models.ForeignKey("Customer", on_delete=models.SET_NULL, null=True)
    gray_receipt_no = models.CharField("Gray Receipt No", max_length=30)
    dc_no = models.CharField("D/C No", max_length=30)
    lot_no = models.CharField("Lot No", max_length=30)
    nature = models.CharField(max_length=30, choices=NATURE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.TextField(blank=True)

            
    class Meta:
        db_table = "lot_transaction"
        verbose_name = 'Lor Transaction'
        verbose_name_plural = 'Lot Transactions'
    
    def __str__(self):
        return f"Lot {self.lot_no} - {self.nature} ({self.doc_no})"
    

class IssueTransaction(models.Model):
    NATURE_CHOICES = [
        ('Issue', 'Issue'),
        ('Return', 'Return'),
        # Add more based on your operations
    ]

    transaction_no = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    nature = models.CharField(max_length=30, choices=NATURE_CHOICES)

    area = models.ForeignKey("AreaForm", on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey("DepartmentDefinition", on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    lot_no = models.CharField("Lot No", max_length=30)
    dc_no = models.CharField("D/C No", max_length=30)
    material = models.CharField(max_length=200, null=True)
    
            
    class Meta:
        db_table = "issue_transaction"
        verbose_name = 'Issue Transaction'
        verbose_name_plural = 'Issue Transactions'
    
    def __str__(self):
        return f"Issue {self.transaction_no} - {self.nature}"
