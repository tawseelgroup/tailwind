from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def mainpage(request):
    return render(request, 'mainpage.html')

class Accounting(TemplateView):
    template_name = 'accounting.html'
    

class Hr(TemplateView):
    template_name = 'hr.html'
    
class Production(TemplateView):
    template_name = 'production.html'
    
    
    
