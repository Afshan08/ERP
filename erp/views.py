from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from .area_form import Area
from .supplier_form import SupplierForm
from .customer_form import CustomerForm
from .customer_model_form import CustomerModelForm
from .models import AreaForm, Supplier, Customer
from sqlite3 import IntegrityError

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
                area = AreaForm.objects.create(areacode=area_code, areaname=area_name, area_description=area_description, status=status)
                form = Area()
                message = f"Area {area_name} successfully created. "
            except AreaForm.DoesNotExist:
                error = "Something went wrong. Area not found."
                
                
            except Exception as e:
                taken_area = AreaForm.objects.get(areacode=area_code)
                error = f"The area code was taken for {taken_area.areaname}"
          
    else:
        form = Area()
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
    form = SupplierForm()
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
    form = CustomerModelForm()
    message = None
    error = None
    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            # Process the valid form data using ModelForm's save method
            customer = form.save()
            form = CustomerModelForm()  # Reset form after successful save
            message = f"Customer {customer.customer_name} successfully created."
        else:
            error = "Please correct the errors below."

    return render(request, "customer_form.html", {
        "form": form,
        "message": message,
        "errors": error,
    })
