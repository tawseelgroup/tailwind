from django.db import models
from django.urls import reverse

# Create your models here.

class Item(models.Model):
    # PACKAGING_TYPE= [
    #     ("pkg", "Package"),
    #     ("bar", "Barrel"),
    #     ("bag", "Bag"),
    #     ("drm", "Drum"),
    #     ("boc", "Box"),
    #     ("num", "Number"),
    #     ("tnk", "Tank"),
    # ]
    
    UNIT = [
        ('kg', 'Kilogram'),
        ('bar', 'Barrel'),
        ('box', 'Box'),
        ('drm', 'Drum'),
        ("crt", "cartoon"),
    ]
    itemName = models.CharField(max_length=50)
    unit = models.CharField(max_length=3, choices=UNIT)
    
    # packing = models.CharField(max_length=3, choices=PACKAGING_TYPE)
    # count = models.IntegerField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.itemName

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})
    
 
    
class Material(Item):
    
    

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Material_detail", kwargs={"pk": self.pk})


