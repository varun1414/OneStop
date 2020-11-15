from django.shortcuts import render
from django.db import connection
from general import models as models
from general.models import Customer,Orders
from django.http import HttpResponse
from django.db.models import Sum
def registersb(request):
    f=1
    email=request.POST.get('email',False)
    name=request.POST.get('name',False)
    pwd=request.POST.get('password',False)
    add=request.POST.get('address',False)
    city=request.POST.get('city',False)
    zip=request.POST.get('zip',False)
    add = str(add) + str(city) + str(zip)
    phno=request.POST.get('phno',False)
    cursor = connection.cursor()

    val = (name,add,phno,email)
    sql = "INSERT INTO customer (customer_name,address,contact,email) values (%s ,%s,%s, %s)"
    cursor.execute(sql,val)
    cust = models.Customer.objects.last()

    c_id = cust.cust_id
    
    val = (email,pwd,c_id)
    sql = "INSERT INTO loginc (email,password,cust_id) values (%s ,%s,%s)"
    cursor.execute(sql,val)
    
    return render(request,'./general/login.html',{'f':f})

def loginsb(request):
    cursor = connection.cursor()
    email=request.POST['email']
    password=request.POST['password']
    f=0
    if models.Loginc.objects.all().values('email').filter(email=email):
        p=models.Loginc.objects.get(email=email).password
        if p==password:
            f=1
        else :
            f=0
    else :
        print('email does not exist')

    if f==1:    
       
        cust_id = models.Customer.objects.all().values('cust_id').filter(email=email)[0]['cust_id']
        
        request.session['email']=email 
        
        cart = models.Orders.objects.filter(cust_id=cust_id).aggregate(Sum('quantity'))
        cart = cart['quantity__sum']
      
        if(cart==None):
            cart=0
        
        request.session['cart']= cart
        request.session['cust_id'] = cust_id
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        quant = models.Orders.objects.all().filter(cust_id=cust_id)
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':1})
    else :
        return render(request,'./general/login.html')

def products(request,category):
    cursor = connection.cursor()
    cust_id = request.session['cust_id']
    cart = request.session['cart']
    if category == 'clothing':
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':1})
    elif category == 'pc':
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':2})
    elif category == 'yummies':
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':3})
    elif category == 'hd':
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':4})
    else:
        product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
        product = cursor.fetchall()
        return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':5})
   
def addtocart(request,pro_id):  
    cust_id = request.session['cust_id']
    quantity = models.Product.objects.all().values('quantity').filter(pro_id=pro_id)[0]['quantity']
    cursor = connection.cursor()
    
    if(quantity>=1):
        is_available=1
        request.session['cart'] = request.session['cart'] + 1
        try:
            print(models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity'])
            quant_order=models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity']
    
            amount = models.Orders.objects.all().values('amount').filter(pro_id=pro_id,cust_id=cust_id)[0]['amount']
           
            amount = amount + (amount/quant_order)
            
            quant_order = models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity'] + 1
            cursor = connection.cursor()
            cursor.execute("update orders set quantity = %s,amount=%s where pro_id = %s and cust_id=%s",[quant_order,amount,pro_id,cust_id])
        except:
            cursor = connection.cursor()
            amount = models.Product.objects.all().values('price').filter(pro_id=pro_id)[0]['price']
            val = (cust_id,pro_id,1,amount)
            sql = "INSERT INTO orders (cust_id,pro_id,quantity,amount) values (%s ,%s,%s, %s)"
            cursor.execute(sql,val)
        q = models.Product.objects.all().values('quantity').filter(pro_id=pro_id)[0]['quantity']
        q-=1
        if q==0:
            is_available=0
        cursor.execute("update product set quantity = %s where pro_id = %s",[q,pro_id])
        
    else:
        is_available=0
        #if the product exists in the order table
    category_id = models.Product.objects.all().values('category_id').filter(pro_id=pro_id)[0]['category_id']    
    product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
    product = cursor.fetchall()
    cart= request.session['cart']
    return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':category_id})

def removefromcart(request,pro_id):
    cursor = connection.cursor()
    cust_id=request.session['cust_id']
    quant_order=models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity']
    quant_product=models.Product.objects.all().values('quantity').filter(pro_id=pro_id)[0]['quantity']
    cursor.execute('delete from orders where pro_id=%s and cust_id=%s',[pro_id,cust_id])
    quant_total=quant_order + quant_product
    request.session['cart']-=quant_order
    cursor.execute("update product set quantity = %s where pro_id = %s",[quant_total,pro_id])
    #product = models.Orders.objects.all().filter(cust_id=cust_id)
    product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders INNER JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
    product = cursor.fetchall()    
    return render(request,'user/checkout.html',{'cart':request.session['cart'],'cust_id':cust_id,'product':product})

def checkout(request):
    cursor = connection.cursor()
    cust_id = request.session['cust_id']
    cart = request.session['cart']
    product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders INNER JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
    product = cursor.fetchall()
    return render(request,'user/checkout.html',{'cart':request.session['cart'],'cust_id':cust_id,'product':product})       
        
def decrementitem(request,pro_id):
    cust_id = request.session['cust_id']
    cursor = connection.cursor()
    qp=models.Product.objects.all().values('quantity').filter(pro_id=pro_id)[0]['quantity']

    try:
        q=models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity']
        if q==1:
            request.session['cart']-=1
            cursor.execute('delete from orders where pro_id=%s and cust_id=%s',[pro_id,cust_id])
            cursor.execute("update product set quantity = %s where pro_id = %s",[qp+1,pro_id])
            
        else: 
            request.session['cart']-=1    
            cursor.execute("update product set quantity = %s where pro_id = %s",[qp+1,pro_id]) 
            amount = models.Orders.objects.all().values('amount').filter(pro_id=pro_id,cust_id=cust_id)[0]['amount']
            amount = amount - (amount/q)
            q=q-1
            cursor.execute("update orders set quantity = %s where pro_id = %s and cust_id=%s",[q,pro_id,cust_id])
            cursor.execute("update orders set amount = %s where pro_id = %s and cust_id=%s",[amount,pro_id,cust_id])
            
        print(models.Orders.objects.all().values('quantity').filter(pro_id=pro_id,cust_id=cust_id)[0]['quantity'])
        
    except:
        is_decrement=0
    
    category_id = models.Product.objects.all().values('category_id').filter(pro_id=pro_id)[0]['category_id']    
    product= cursor.execute("SELECT product.name,product.description,orders.quantity,product.category_id,product.price,orders.cust_id,product.pro_id FROM orders RIGHT JOIN product ON orders.pro_id = product.pro_id and orders.cust_id=%s",[cust_id])
    product = cursor.fetchall()
    cart= request.session['cart']
    return render(request,'./general/mainpage.html',{'cart':cart,'product':product,'cust_id':cust_id,'category_id':category_id})
