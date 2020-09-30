from django.urls import path,include
from .views import home,aboutPage

urlpatterns = [
    path('', home, name = 'home'),
    path('about/',aboutPage,name = 'about')

]