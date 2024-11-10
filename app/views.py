from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CompanyForm

# Create your views here.


def mainpage(request):
    return render(request, 'mainpage.html')

class Accounting(TemplateView):
    template_name = 'accounting.html'
    

class Hr(TemplateView):
    template_name = 'hr.html'
    
class Production(TemplateView):
    template_name = 'production.html'
    
def companies(request):
    form = CompanyForm
    return render(request, 'companies.html', {'form': form})
    
    
    
