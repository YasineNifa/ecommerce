from django.urls import path,include
from .views import home,productPage

urlpatterns = [
    path('', home, name = 'home'),
    path('<slug:category_slug>',home,name = 'product_by_category'),
    path('product/',productPage,name = 'product')

]