from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):    
    class Meta:
        model = Company
        fields = ('cname', 'loc', 'tradeRec')
        
        widgets = {
            'cname' : forms.TextInput(attrs={'class': 'input-control'}),
            'loc' : forms.TextInput(attrs={'class': 'input-control'}),
            'tradeRec' : forms.TextInput(attrs={"class": 'input-styles'}),
        }
        

