from os import name
from django.db import models

class product(models.Model):
    name = models.CharField(max_length=999999999)
    description=models.TextField()
    vip = models.BooleanField(default=False)
    price=models.IntegerField(max_length=1000,default=0)
    images=models.ImageField(upload_to="product_pic" , default=None)
    offer_perc=models.FloatField(default=0.0)    
    def __str__(self): 
        return "[Vip]"+self.name if self.vip else self.name

    def final_price(self):
        final_p = (float(self.price)*self.offer_perc/100)
        return (self.price-final_p)