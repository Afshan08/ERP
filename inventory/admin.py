from django.contrib import admin
from .models import AreaForm, Supplier, Customer, Purchase, INVcategory, DepartmentDefinition
admin.site.register(AreaForm)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(INVcategory)
admin.site.register(DepartmentDefinition)