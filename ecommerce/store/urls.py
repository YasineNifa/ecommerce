from django.urls import path,include
from .views import home,productPage

urlpatterns = [
    path('', home, name = 'home'),
    path('category/<slug:category_slug>',home,name = 'product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',productPage,name = 'product_detail')

]