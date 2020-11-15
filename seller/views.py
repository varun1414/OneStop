from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from general.models import Sells,Product,Category,Seller,Logins
from django.contrib.auth.hashers import make_password
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
    product=[]
    p=Product(name=pname,image=image,price=cost,description=desc,quantity=quant,category_id=category_id)
    p.save()
    s=Sells(p.pro_id,seller_id=request.session['uid']) 
    s.save()
    pid=Sells.objects.filter(seller_id=request.session['uid']).values()  
            
    for i in pid:
        product.append(Product.objects.values().filter(pro_id=i['pro_id']))
    
   
    
    return HttpResponseRedirect('/seller/editSuccess/%d' %p.pro_id)


def register_page(request):
    return render(request,"seller/register.html")

def registerdone(request):
    email=request.POST.get('email')
    name=request.POST.get('name')
    password=request.POST.get('password')
    address=request.POST.get('address')
    city=request.POST.get('city')
    zip=request.POST.get('zip')
    pno=request.POST.get('pno')


    n=Seller(seller_name=name,address=address,contact=pno,email=email)
    n.save()
    m=Logins(seller_id=n.seller_id,email=email,password=make_password(password))
    m.save()
    return render(request,'general/login.html')


def edit(request,pro_id):
    product=Product.objects.get(pro_id=int(pro_id))
    # category=Category.objects.get(name=pr)
    category=Category.objects.get(category_id=product.category_id)
    return render(request,'seller/editproduct.html',{'product':product,'category':category})

def editDone(request,pro_id):
    pname=request.POST.get('name',False)
    image=request.POST.get('image',False)
    cost=request.POST.get('cost',False)
    category=request.POST.get('category',False)
    desc=request.POST.get('des',False)
    quant=request.POST.get('quant',False)
    product=[]
    #  pname=request.POST.get('image',False)
    if category != False:
        category_id=Category.objects.get(name=category).get_id
        product=[]
        p=Product.objects.get(pro_id=pro_id)
        p.name=pname
        p.image=image
        p.price=cost
        p.description=desc
        p.quantity=quant
        p.category_id=category_id
        p.save()
        s=Sells(p.pro_id,seller_id=request.session['uid']) 
        s.save()
    pid=Sells.objects.filter(seller_id=request.session['uid']).values()  
            
    for i in pid:
        product.append(Product.objects.values().filter(pro_id=i['pro_id']))

    return render(request,'seller/mainpage.html',{'uname':request.session['uname'],'product':product})


def delete(request,pro_id):
    p=Product.objects.get(pro_id=pro_id)
    p.delete()
    product=[]
    pid=Sells.objects.filter(seller_id=request.session['uid']).values()  
    for i in pid:
        product.append(Product.objects.values().filter(pro_id=i['pro_id']))

    return render(request,'seller/mainpage.html',{'uname':request.session['uname'],'product':product})
