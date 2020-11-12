
from . import views


from django.urls import path,include
urlpatterns = [
    path('',views.login),
    path('auth/',views.auth),
    path('seller/',include('seller.urls'))
    ]