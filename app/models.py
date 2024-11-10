from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    cname = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)
    tradeRec = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"

    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})
    


