from django.urls import path,include
from . import views 
urlpatterns = [
    # path('',views.home),
   path('addproduct/',views.add_product),
   path('productSuccess/',views.productadded),
   path('register/',views.register_page),
   path('registerdone/',views.registerdone)
   
   ]
