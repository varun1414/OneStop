from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from . import models
def login(request):
    
    return render(request,'general/login.html')
# Create your views here.


def auth(request):
    uid=request.POST.get('username',False)
    passw=request.POST.get('password',False)

    if models.Logins.objects.all().values('seller_id').filter(seller_id=1):
        print("login")
        p=models.Logins.objects.get(seller_id=uid).passw

        print(p)
        
        print(check_password(passw,p))
        if (check_password(passw,p)):
            name=models.Seller.objects.get(seller_id=uid)
            request.session['uid']=uid    
            return render(request,'./seller/profile.html',{'uname':name})

    
    
    return HttpResponse("hellop")
    

