from django.urls import path
from app.views import Production, Hr, Accounting, mainpage, companies

app = 'app'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('production/', Production.as_view(), name='production'),
    path('hr/', Hr.as_view(), name='hr'),
    path('accounting/', Accounting.as_view(), name='accounting'),
    path('companies/', companies, name='companies'),
]
