from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import request
from .models import product

p = Paginator(product.objects.all(),3)
def mainpage(request):
    
    return render(request,'store/index.html', 
    {
        'products':p.get_page(request.GET.get("page")),
    }
    )

def productpage(request,product_name):
    return render(request,'store/product.html',
    
    {
        'product':product.objects.get(name=product_name),
    }
    
    )