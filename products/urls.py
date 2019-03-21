from django.urls import path,include
from . import views

urlpatterns = [


    path('products/',views.product_list),
    path('products/<pk>',views.product_detail),

    
]