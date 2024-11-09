from django.urls import path
from .views import Dashboard, purchase,  manufactoring, sales, disbursement, inventory, purchased, dash, po, suppliers, products

app = "store"

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('purchase/', purchase, name='purchase'),
    path('inventory/', inventory, name='inventory'),
    path('sales/', sales, name='sales'),
    path('manufactoring/', manufactoring, name='manufactoring'),
    path('disbursement/', disbursement, name='disbursement'),
    path('purchase/', purchase, name='purchase'),
    
    
    path('purchase/dash/', dash, name='dash'),
    path('purchase/po/', po, name='po'),
    path('purchase/purchased/', purchased, name='purchased'),
    path('purchase/suppliers/', suppliers, name='suppliers'),
    path('purchase/products/', products, name='products'),
]
