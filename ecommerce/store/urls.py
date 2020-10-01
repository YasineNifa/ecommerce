from django.urls import path,include
from .views import home,productPage

urlpatterns = [
    path('', home, name = 'home'),
    path('product/',productPage,name = 'product')

]