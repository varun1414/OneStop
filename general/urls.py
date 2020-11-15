
from . import views

from user import views as viewsb
from django.urls import path,include
urlpatterns = [
    path('',views.login),
    path('logins/',views.logins),
    path('auth/',views.auth),
    path('seller/',include('seller.urls')),

        
    path('register/',views.register),
    path('seller/',include('seller.urls')),
    
    #User
    path('registersb/',viewsb.registersb),
    path('loginsb/',viewsb.loginsb),
    path('products/<str:category>',viewsb.products),
    path('addtocart/<int:pro_id>',viewsb.addtocart),
    path('checkout/',viewsb.checkout),
    path('removefromcart/<int:pro_id>',viewsb.removefromcart),
    path('decrementitem/<int:pro_id>',viewsb.decrementitem),
    ]