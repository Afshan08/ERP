from django.shortcuts import redirect

def home(request):
    return redirect('inventory/area_form')

