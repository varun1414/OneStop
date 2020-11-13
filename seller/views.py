from django.shortcuts import render,HttpResponse
from general.models import Sells,Product,Category
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
    quant=request.POST.get('quant',False)
    #  pname=request.POST.get('image',False)
    category_id=Category.objects.get(name=category).get_id
    
    p=Product(name=pname,image=image,price=cost,description=desc,quantity=quant,category_id=category_id)
    p.save()
    s=Sells(p.pro_id,seller_id=request.session['uid']) 
    s.save()
    

    return render(request,'seller/profile.html',{'uname':request.session['uname']})