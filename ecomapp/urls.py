from django.urls import path
from ecomapp.views import *
from ecomapp import views

app_name = 'ecomapp'

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("shoestore/", ShoeView.as_view(), name='shoestore'),
    path("menstore/", MenView.as_view(), name='menstore'),
    path("womenstore/", WomenView.as_view(), name='womenstore'),
    path("productview/<slug:slug>/", ProductView.as_view(), name='productview'),
    path('addtocart/', views.AddToCart, name='addtocart'),
    path('cart/', views.CartView, name='cart'),
    path('login/', views.LogIn, name='login'),
    path('signin/', views.SignIn, name='signin'),
    path('logout/', views.LogOut, name='logout'),
    
]