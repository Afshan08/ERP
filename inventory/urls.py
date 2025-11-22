"""
URL configuration for erp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("area_form", views.area_form ,name="area_form"),
    path("", views.home, name="home_page"),
    path("supplier_form", views.supplier_form, name="supplier_form"),
    path("customer_form", views.customer_form, name="customer_form"),
    path("purchase_form", views.purchase_form, name="purchase_form"),
    path("department_definition", views.department_definition, name="department_definition"),
    path("inv_category", views.inventory_category, name="inv_category"),
    path("item_definition", views.item_definition_form, name="item_definition"),
    path("requisition", views.requisition_form, name="requisition_form"),
    path("purchase_order", views.purchase_order_form, name="purchase_order_form"),
    path("receipt_transaction", views.receipttransaction_form, name="receipttransaction_form"),
    path("purchase_voucher", views.purchasevoucher_form, name="purchasevoucher_form"),
    path("lot_transaction", views.lottransaction_form, name="lottransaction_form"),
    path("issue_transaction", views.issuetransaction_form, name="issuetransaction_form"),
    
    # Lookup URLs for search functionality
    path("lookup_supplier/", views.lookup_supplier, name="lookup_supplier"),
    path("lookup_requisition/", views.lookup_requisition, name="lookup_requisition"),
    path("lookup_area/", views.lookup_area, name="lookup_area"),
    path("lookup_item/", views.lookup_item, name="lookup_item"),
    path("lookup_purchase_order/", views.lookup_purchase_order, name="lookup_purchase_order"),
    path("lookup_customer/", views.lookup_customer, name="lookup_customer"),
    path("lookup_department/", views.lookup_department, name="lookup_department"),
    path("lookup_inventory_category/", views.lookup_inventory_category, name="lookup_inventory_category"),
]
