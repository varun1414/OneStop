from django.urls import path,include
from . import views 
urlpatterns = [
    # path('',views.home),
   path('addproduct/',views.add_product),
   path('productSuccess/',views.productadded),
   path('register/',views.register_page),
   path('registerdone/',views.registerdone),
   path('edit/<str:pro_id>',views.edit),
   path('delete/<str:pro_id>',views.delete),
   path('editSuccess/<str:pro_id>',views.editDone)
   
   ]
