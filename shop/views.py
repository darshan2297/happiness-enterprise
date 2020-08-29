from django.shortcuts import render
from django.views.generic import View
from .models import product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class homepageview(View):
    def get(self,request,*args,**kwargs):
        products = product.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(products,40)
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)
        return render(request ,"home.html",{"product_list":product_list})
        
class product_view(View):
    def get(self,request,pk,*args,**kwargs):
        product_detail = product.objects.filter(id=pk)
        return render(request ,"product_view.html",{"product_detail":product_detail})
