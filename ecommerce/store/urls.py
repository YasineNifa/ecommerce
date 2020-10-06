from django.urls import path,include
from .views import home,productPage,cart_detail,add_cart,cart_remove,cart_trash,search

urlpatterns = [
    path('', home, name = 'home'),
    path('category/<slug:category_slug>',home,name = 'product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',productPage,name = 'product_detail'),
    
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart', cart_detail,name ='cart_detail'),
    path('cart/remove/<int:product_id>',cart_remove,name='cart_remove'),
    path('cart/trash/<int:product_id>',cart_trash,name='cart_trash'),
    path('search/',search,name='search'),

]