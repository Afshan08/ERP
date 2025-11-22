from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .area_definition import Area
from .supplier_form import SupplierForm
from .customer_form import CustomerForm
from .customer_model_form import CustomerModelForm
from .purchase_form import PurchaseModelForm
from .inventory_category_form import INVCategory
from .department_definition import Department
from .item_definition_form import ItemDefinitionForm
from .models import AreaForm, Supplier, Customer, Purchase, DepartmentDefinition, Requisition, PurchaseOrder
from .requisition_form import RequisitionForm
from .purchase_order_form import PurchaseOrderForm
from .receipttransaction_form import GRNForm
from .purchasevoucher_form import PurchaseVoucherForm
from .lottransaction_form import LotTransactionForm
from .issuetransaction_form import IssueTransactionForm
from sqlite3 import IntegrityError
from .utils import generate_code
from .models import ItemDefinition, ReceiptTransaction, IssueTransaction, LotTransaction, PurchaseVoucher

def area_form(request):
    if request.method == 'POST':
        form = Area(request.POST)
        message = None
        error = None
        if form.is_valid():
            area_code = form.cleaned_data['area_code']
            area_name = form.cleaned_data['area_name']
            area_description = form.cleaned_data['area_description']
            status = form.cleaned_data['status']
            
            
            
            try:
                if not area_code:
                    area_code = generate_code(AreaForm, 'AREA', 'area_code')
                area = AreaForm.objects.create(areacode=area_code, areaname=area_name, area_description=area_description, status=status)
                form = Area()
                message = f"Area {area_name} successfully created. "
            except AreaForm.DoesNotExist:
                error = "Something went wrong. Area not found."
                
                
            except Exception as e:
                taken_area = AreaForm.objects.get(areacode=area_code)
                error = f"The area code was taken for {taken_area.areaname}"
          
    else:
        initial_data = {}
        next_code = generate_code(AreaForm, 'AREA', 'area_code')
        initial_data['area_code'] = next_code
        form = Area(initial=initial_data)
        message = None
        error = None

    return render(request, 'area.html', {
        'form': form,
        "message": message,
        "errors": error,
        })
    
def home_page(request):
    return redirect("area_form")


def home(request):
    
    return render(request, "index.html")


def supplier_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(Supplier, 'SUP', 'supplier_code')
        initial_data['supplier_code'] = next_code
        
    form = SupplierForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = SupplierForm(request.POST)
    if form.is_valid():
        ntn_number = form.cleaned_data['ntn_number']
        try:
            supplier = Supplier(
                supplier_id=form.cleaned_data['supplier_id'],
                supplier_name=form.cleaned_data['supplier_name'],
                contact_person_name=form.cleaned_data['contact_person_name'],
                contact_email=form.cleaned_data['contact_email'],
                contact_phone=form.cleaned_data['contact_phone'],
                business_type=form.cleaned_data['business_type'],
                ntn_number=ntn_number if ntn_number else None,
                country=form.cleaned_data['country'],
                payment_terms=form.cleaned_data['payment_terms'],
                currency=form.cleaned_data['currency'],
                website=form.cleaned_data['website'] if form.cleaned_data['website'] else None,
                notes=form.cleaned_data['notes'] if form.cleaned_data['notes'] else None,
                status=form.cleaned_data['status'],
                is_preferred=form.cleaned_data['is_preferred']
            )
            if not supplier.supplier_code:
                supplier.supplier_code = generate_code(Supplier, 'SUP', 'supplier_code')
            supplier.save()
            form = SupplierForm()  # Reset form after successful save
            message = f"Supplier {supplier.supplier_name} successfully created."
        except Exception as e:
            error = "Supplier with this ID already exists."
            

    return render(request, "supplier_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })
        
        
def customer_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(Customer, 'CUST', 'customer_code')
        initial_data['customer_code'] = next_code

    form = CustomerModelForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            customer = form.save(commit=False)
            if not customer.customer_code:
                customer.customer_code = generate_code(Customer, 'CUST', 'customer_code')
            customer.save()
            form = CustomerModelForm()  # Reset form after successful save
            message = f"Customer {customer.customer_name} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "customer_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })


def purchase_form(request):
    form = PurchaseModelForm()
    message = None
    error = None
    if request.method == "POST":
        form = PurchaseModelForm(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            purchase = form.save()
            form = PurchaseModelForm()  # Reset form after successful save
            message = f"Purchase {purchase.purchase_id} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "purchase_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })


def department_definition(request):
    form = Department()
    message = None
    error = None
    if request.method == "POST":
        form = Department(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            department = form.save()
            form = Department()  # Reset form after successful save
            # message = f"Customer {department.name} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "department_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })
    
    
def inventory_category(request):    
    form = INVCategory()
    message = None
    error = None
    if request.method == "POST":
        form = INVCategory(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            inv_category = form.save()
            form = INVCategory()  # Reset form after successful save
            # message = f"Customer {department.name} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "inventory_category.html", {
        "form": form,
        "message": message,
        "errors": error,
    })


def item_definition_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(ItemDefinition, 'ITEM', 'item_code')
        initial_data['item_code'] = next_code
        
    form = ItemDefinitionForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = ItemDefinitionForm(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            item = form.save()
            form = ItemDefinitionForm()  # Reset form after successful save
            message = f"Item {item.item_name} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "item_definition.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def requisition_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(Requisition, 'REQ', 'doc_number')
        initial_data['doc_number'] = next_code
        
    form = RequisitionForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = RequisitionForm(request.POST)
        if form.is_valid():
            requisition = form.save()
            form = RequisitionForm()
            message = f"Requisition {requisition.doc_number} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "requisition_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def purchase_order_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(PurchaseOrder, 'PO', 'po_number')
        initial_data['po_number'] = next_code
        
    form = PurchaseOrderForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            purchase_order = form.save()
            form = PurchaseOrderForm()
            message = f"Purchase Order {purchase_order.po_number} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "purchase_order_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def receipttransaction_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(ReceiptTransaction, 'GRN', 'transaction_no')
        initial_data['transaction_no'] = next_code
        
    form = GRNForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = GRNForm(request.POST)
        if form.is_valid():
            receipt = form.save()
            form = GRNForm()
            message = f"Receipt Transaction {receipt.transaction_no} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "receipttransaction_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def purchasevoucher_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(PurchaseVoucher, 'PV', 'transaction_no')
        initial_data['transaction_no'] = next_code
        
    form = PurchaseVoucherForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = PurchaseVoucherForm(request.POST)
        if form.is_valid():
            voucher = form.save()
            form = PurchaseVoucherForm()
            message = f"Purchase Voucher {voucher.transaction_no} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "purchasevoucher_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def lottransaction_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(LotTransaction, 'LOT', 'doc_no')
        initial_data['doc_no'] = next_code
        
    form = LotTransactionForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = LotTransactionForm(request.POST)
        if form.is_valid():
            lot = form.save()
            form = LotTransactionForm()
            message = f"Lot Transaction {lot.doc_no} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "lottransaction_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })

def issuetransaction_form(request):
    initial_data = {}
    if request.method == "GET":
        next_code = generate_code(IssueTransaction, 'ISS', 'transaction_no')
        initial_data['transaction_no'] = next_code
        
    form = IssueTransactionForm(initial=initial_data)
    message = None
    error = None
    if request.method == "POST":
        form = IssueTransactionForm(request.POST)
        if form.is_valid():
            issue = form.save()
            form = IssueTransactionForm()
            message = f"Issue Transaction {issue.transaction_no} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "issuetransaction_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })


# Lookup views for search functionality
def lookup_supplier(request):
    """Return supplier data for lookup modal"""
    suppliers = Supplier.objects.all().values(
        'id', 
        'supplier_name', 
        'contact_person_name', 
        'contact_email', 
        'contact_phone'
    )
    return JsonResponse(list(suppliers), safe=False)


def lookup_requisition(request):
    """Return requisition data for lookup modal"""
    requisitions = Requisition.objects.select_related('department').all()
    data = [{
        'id': req.id,
        'doc_number': req.doc_number,
        'requisition_by': req.requisition_by,
        'department_name': req.department.name
    } for req in requisitions]
    return JsonResponse(data, safe=False)


def lookup_area(request):
    """Return area data for lookup modal"""
    areas = AreaForm.objects.all().values(
        'id',
        'areacode',
        'areaname',
        'area_description'
    )
    return JsonResponse(list(areas), safe=False)


def lookup_item(request):
    """Return item data for lookup modal"""
    from .models import ItemDefinition
    items = ItemDefinition.objects.select_related('item_category').all().values(
        'id',
        'item_code',
        'item_name',
        'specification',
        'unit_of_measure',
        'item_category__name'
    )
    return JsonResponse(list(items), safe=False)


def lookup_purchase_order(request):
    """Return purchase order data for lookup modal"""
    pos = PurchaseOrder.objects.select_related('supplier', 'requisition').all().values(
        'id',
        'po_number',
        'supplier__supplier_name',
        'requisition__doc_number'
    )
    return JsonResponse(list(pos), safe=False)


def lookup_customer(request):
    """Return customer data for lookup modal"""
    customers = Customer.objects.all().values(
        'id',
        'customer_name',
        'contact_person_name',
        'contact_phone'
    )
    return JsonResponse(list(customers), safe=False)


def lookup_department(request):
    """Return department data for lookup modal"""
    departments = DepartmentDefinition.objects.all().values(
        'id',
        'name',
        'description'
    )
    return JsonResponse(list(departments), safe=False)


def lookup_inventory_category(request):
    """Return inventory category data for lookup modal"""
    categories = INVCategory.objects.all().values(
        'id',
        'name'
    )
    return JsonResponse(list(categories), safe=False)
