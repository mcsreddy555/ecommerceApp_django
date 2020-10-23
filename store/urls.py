from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('show/',views.show,name='show'),
    
    path('update_view/',views.updateItem, name='update_item'),
    path('process_order/',views.processOrder, name='process_order'),
    path('detail_view/',views.productDetails, name='detail_view'),
]
