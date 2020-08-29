from django.shortcuts import render
from django.views.generic import View
from .models import product
# Create your views here.

class homepageview(View):
    def get(self,request,*args,**kwargs):
        products = product.objects.all()
        return render(request ,"home.html",{"products":products})
        
class product_view(View):
    def get(self,request,pk,*args,**kwargs):
        product_detail = product.objects.filter(id=pk)
        return render(request ,"product_view.html",{"product_detail":product_detail})
