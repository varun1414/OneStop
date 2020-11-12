from django.shortcuts import render,HttpResponse
from general.models import Sells,Product
# Create your views here.

def add_product(request):
    return render(request,'seller/addproduct.html')

def home(request):
    return HttpResponse("done")
def productadded(request):
    pname=request.POST.get('name',False)
    image=request.POST.get('image',False)
    cost=request.POST.get('cost',False)
    category=request.POST.get('category',False)
    desc=request.POST.get('des',False)
    #  pname=request.POST.get('image',False)
    s=Product(name=pname,image='',price=1,description='asd',quantity=123,category_id=1)
    s.save()
    return HttpResponse("done")