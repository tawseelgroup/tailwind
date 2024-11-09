from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    


def purchase(request):
    return render(request, 'purchase.html')


def disbursement(request):
    return render(request, 'disbursement.html')

def manufactoring(request):
    return render(request, 'manufactoring.html')

def inventory(request):
    return render(request, 'inventory.html')

def sales(request):
    return render(request, 'sales.html')



def dash(request):
    return render(request, 'purchase/dash.html')

def po(request):
    return render(request, 'purchase/po.html')

def purchased(request):
    return render(request, 'purchase/purchased.html')

def suppliers(request):
    return render(request, 'purchase/suppliers.html')

def products(request):
    return render(request, 'purchase/products.html')